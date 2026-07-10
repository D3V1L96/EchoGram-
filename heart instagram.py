import sys
import os
import logging
import asyncio
import random
import requests
from aiograpi import Client

# ====================== CLEAN LOGGING ======================
class CleanFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage().lower()
        if any(word in msg for word in ["none [200]", "http request", "i.instagram.com", "httpx", "httpcore"]):
            return False
        return True

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("heart_instagram.log", encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
logging.getLogger().addFilter(CleanFilter())

for pkg in ["aiograpi", "httpx", "httpcore"]:
    logging.getLogger(pkg).setLevel(logging.ERROR)

# ====================== GROQ CONFIG ======================
GROQ_API_KEY = "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"   # ← PUT YOUR GROQ KEY HERE
SESSION_FILE = "instagram_session.json"


class HeartInstagram:
    def __init__(self):
        self.cl = Client()
        self.cl.delay_range = [1, 3]
        self.cl.set_locale("en_US")
        self.cl.set_timezone_offset(-19800)

        self.logged_in = False
        self.conversation_history = {}
        self.last_message_ids = {}
        self.user_cache = {}
        self.rt = None

    # ====================== TEST GROQ ======================
    def test_groq(self):
        print("🔍 Testing Groq API...")
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": "Reply only: Groq is working perfectly! ❤️"}],
                    "max_tokens": 50,
                    "temperature": 0.7
                },
                timeout=15
            )
            if response.status_code == 200:
                reply = response.json()['choices'][0]['message']['content'].strip()
                print(f"✅ Groq Working! {reply}")
                return True
            else:
                print(f"❌ Groq Error {response.status_code}: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"⚠️ Groq Test Failed: {e}")
            return False

    async def login(self):
        if os.path.exists(SESSION_FILE):
            try:
                self.cl.load_settings(SESSION_FILE)
                await self.cl.account_info()
                self.logged_in = True
                print("✅ Loaded saved session")
                return True
            except:
                os.remove(SESSION_FILE)

        print("\n" + "=" * 70)
        print("LOGIN IN BROWSER")
        print("=" * 70)
        input("\nPress Enter after login... ")
        sessionid = input("SessionID: ").strip()
        if len(sessionid) < 30:
            print("❌ Invalid sessionid")
            return False

        try:
            await self.cl.login_by_sessionid(sessionid)
            await self.cl.account_info()
            self.cl.dump_settings(SESSION_FILE)
            self.logged_in = True
            print("✅ Login Successful!")
            return True
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False

    # ====================== AI REPLY WITH GROQ ======================
    def _generate_reply_sync(self, sender_username, message, history=None):
        context = "\n".join(history[-8:]) if history else ""
        prompt = f"""You are a calm, mature, emotionally intelligent Indian man in your early 30s.

Speak naturally like a real person, not a therapist, coach, or AI assistant. You understand emotions, relationships, stress, ambition, loneliness, and everyday life experiences. You listen first, then respond thoughtfully.

Use a natural mix of English and Hindi (Hinglish) when it feels appropriate. Never force Hindi into every sentence. Speak the way educated young Indians naturally talk with friends.

Keep responses concise and conversational (10-35 words unless a detailed answer is needed).

When someone shares a problem:

* Acknowledge their feelings naturally.
* Don't immediately jump into solutions.
* Show understanding before giving advice.
* Be honest, practical, and balanced.

Avoid:

* Overly motivational speeches.
* Generic self-help language.
* Sounding like a therapist.
* Excessive enthusiasm.
* Unnecessary emojis.

Use humor occasionally when it fits the situation.

Your tone should feel like:

* A trusted older brother.
* A thoughtful friend.
* Someone who has seen enough life to stay calm under pressure.

The goal is to make people feel understood, respected, and comfortable talking openly.
.

Recent conversation:
{context}

@{sender_username}: {message}

Natural reply:"""

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.3-70b-versatile",   # Very good & fast
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.92,
                    "max_tokens": 180
                },
                timeout=20
            )

            if response.status_code == 200:
                reply = response.json()['choices'][0]['message']['content'].strip()[:180]
                logger.info(f"Groq reply for @{sender_username}: {reply}")
                return reply

        except Exception as e:
            logger.error(f"Groq Error: {e}")

        return random.choice(["Samajh gaya, batao kya baat hai"],"Main yahan hoon, batao")

    async def human_typing_delay(self, text_length: int):
        base = 1.2 if text_length < 40 else 2.4
        await asyncio.sleep(base + random.uniform(0.5, 1.7))

    async def _resolve_username(self, user_id: str) -> str:
        if not user_id or user_id == "0":
            return "friend"
        if user_id in self.user_cache:
            return self.user_cache[user_id]
        try:
            info = await self.cl.user_info(int(user_id))
            username = info.username or info.full_name or "friend"
            self.user_cache[user_id] = username
            return username
        except:
            return f"user_{user_id[-4:]}"

    # ====================== EVENT HANDLER ======================
    def handle_event(self, event_type, payload):
        asyncio.create_task(self._handle_event_async(event_type, payload))

    async def _handle_event_async(self, event_type, payload):
        try:
            if not isinstance(payload, dict):
                return

            if event_type in ["message", "direct"]:
                item = payload.get("message") or payload
                thread_id = payload.get("thread_id") or item.get("thread_id")
                text = item.get("text") if isinstance(item, dict) else None

                user_id = str(item.get("user_id") or payload.get("user_id") or 0)
                username = await self._resolve_username(user_id)
                message_id = item.get("item_id") or item.get("id")

                if not text or not thread_id or user_id == str(self.cl.user_id):
                    return
                if self.last_message_ids.get(user_id) == message_id:
                    return

                self.last_message_ids[user_id] = message_id

                print(f"📩 New from @{username}: {text}")

                if self.rt:
                    try:
                        await self.rt.direct_indicate_activity(thread_id, is_active=True)
                    except:
                        pass

                await self.human_typing_delay(len(text))
                if random.random() < 0.2:
                    await asyncio.sleep(random.uniform(5, 15))

                reply = self._generate_reply_sync(username, text, self.conversation_history.get(username))
                if reply:
                    await self.cl.direct_send(reply, thread_ids=[thread_id])
                    print(f"❤️ To @{username}: {reply}")

                    history = self.conversation_history.setdefault(username, [])
                    history.extend([f"They: {text}", f"You: {reply}"])
                    if len(history) > 16:
                        history.pop(0)

            else:
                user_id = str(payload.get("user_id") or 0)
                username = await self._resolve_username(user_id)
                print(f"🔔 Activity from @{username} | Type: {event_type}")

        except Exception as e:
            logger.error(f"Handler error: {e}")

    # ====================== MAIN ======================
    async def run(self):
        if not self.test_groq():
            print("⚠️ Continuing anyway...")

        if not await self.login():
            return

        print("\n" + "=" * 95)
        print("❤️ HEART INSTAGRAM BOT — GROQ MODE (Fast)")
        print("✅ Real Username Resolution + Groq")
        print("=" * 95 + "\n")

        try:
            self.rt = await self.cl.realtime_connect()

            self.cl.realtime_on("message", lambda p: self.handle_event("message", p))
            self.cl.realtime_on("direct", lambda p: self.handle_event("direct", p))
            self.cl.realtime_on("activity", lambda p: self.handle_event("activity", p))

            await self.rt.direct_subscribe()

            print("🎧 Listening...")

            while True:
                try:
                    await self.cl.realtime_read_once()
                    if random.random() < 0.1:
                        await self.rt.ping()
                except asyncio.TimeoutError:
                    await asyncio.sleep(0.2)
                except Exception:
                    await asyncio.sleep(3)

        except KeyboardInterrupt:
            print("\n🛑 Stopped.")
        except Exception as e:
            logger.error(f"Fatal: {e}")
        finally:
            if self.rt:
                try:
                    await self.cl.realtime_disconnect()
                except:
                    pass


if __name__ == "__main__":
    asyncio.run(HeartInstagram().run())