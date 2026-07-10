# EchoGram AI
### Intelligent Instagram AI Auto-Reply System

> An AI-powered Instagram automation platform that listens to incoming direct messages in real-time and generates natural, context-aware human conversations using Large Language Models.

Developed by **D4RK D3V1L**

---

# Overview

EchoGram AI is a real-time Instagram assistant built with Python that combines Instagram's realtime messaging system with modern Large Language Models to create conversations that feel natural instead of robotic.

Unlike traditional keyword-based chatbots, EchoGram understands previous conversations, user context, emotional tone, and generates intelligent replies while simulating realistic human behavior.

The system securely authenticates using Instagram SessionID, maintains persistent sessions, filters duplicate events, and responds with realistic typing delays.

---

# Features

- Real-time Instagram Message Listener
- AI Powered Conversations (Groq LLM)
- Human-like Typing Simulation
- Persistent Conversation Memory
- Session Authentication
- Duplicate Message Detection
- User Cache System
- Automatic Username Resolution
- Activity Detection
- Clean Logging System
- Password Protected Application
- Animated Terminal Interface
- Automatic Reconnection Support
- Secure Session Storage
- Multi-thread Conversation Support

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Backend |
| aiograpi | Instagram API |
| asyncio | Asynchronous Processing |
| Groq API | AI Response Generation |
| Llama 3.3 70B | Large Language Model |
| Requests | REST Communication |
| Logging | Event Monitoring |
| JSON Session | Persistent Login |

---

# Project Architecture

```
Instagram User
        │
        ▼
Instagram Direct Message
        │
        ▼
Realtime Listener (aiograpi)
        │
        ▼
Event Handler
        │
        ▼
Message Validation
        │
        ▼
Conversation Memory
        │
        ▼
Prompt Builder
        │
        ▼
Groq LLM
        │
        ▼
AI Response
        │
        ▼
Human Typing Delay
        │
        ▼
Instagram Reply
```

---

# Working Mechanism

## 1. Application Startup

When EchoGram starts, it performs several initialization steps:

- Displays animated startup banner
- Shows motivational quotes
- Password authentication
- Loads configuration
- Initializes logging system

---

## 2. Authentication

The application first checks for an existing Instagram session.

If available:

```
Load Session
↓

Verify Session

↓

Login Successful
```

Otherwise:

```
Browser Login

↓

User provides SessionID

↓

Instagram Authentication

↓

Session Saved
```

This avoids repeated logins while maintaining secure authentication.

---

## 3. Realtime Connection

After successful authentication:

- Connects to Instagram Realtime API
- Subscribes to Direct Messages
- Subscribes to Activity Events
- Starts continuous event listening

---

## 4. Incoming Message Detection

Whenever someone sends a DM:

```
Incoming Message

↓

Realtime Event

↓

Extract Thread ID

↓

Extract User ID

↓

Extract Message

↓

Validate Event
```

The system ignores:

- Empty messages
- Duplicate messages
- Self messages
- Invalid events

---

## 5. User Resolution

Instagram only provides User IDs.

EchoGram automatically resolves:

```
User ID

↓

Instagram User Info

↓

Username Cache

↓

Readable Username
```

Caching prevents repeated API requests.

---

## 6. Conversation Memory

For every user, the system stores recent conversations:

```
User

↓

Conversation History

↓

Last 8 Messages

↓

Prompt Context
```

This enables contextual conversations instead of isolated responses.

---

## 7. Prompt Engineering

A dynamic prompt is created using:

- Current message
- Previous conversation
- Username
- Personality instructions
- Emotional context

This ensures replies remain consistent and human-like.

---

## 8. AI Response Generation

The prompt is sent to Groq API using:

```
Model:
Llama 3.3 70B Versatile
```

The AI generates:

- Natural
- Context-aware
- Emotional
- Short conversational replies

---

## 9. Human Behavior Simulation

Instead of replying instantly:

- Typing delay
- Random waiting time
- Activity indication
- Variable response speed

This prevents the account from appearing automated.

---

## 10. Reply Delivery

After delay:

```
Generated Response

↓

Instagram API

↓

Direct Message Sent

↓

Conversation Saved
```

---

# System Flow

```
Start Application
        │
        ▼
Password Verification
        │
        ▼
Load Instagram Session
        │
        ▼
Realtime Connection
        │
        ▼
Wait for Message
        │
        ▼
Receive Event
        │
        ▼
Validate Message
        │
        ▼
Load Conversation
        │
        ▼
Generate AI Prompt
        │
        ▼
Groq LLM
        │
        ▼
Generate Response
        │
        ▼
Typing Delay
        │
        ▼
Send Reply
        │
        ▼
Update Conversation Memory
        │
        ▼
Continue Listening
```

---

# Security Features

- Password Protected Startup
- Secure Session Storage
- Duplicate Event Prevention
- Filtered Logging
- User Cache Protection
- Session Validation
- Controlled API Requests

---

# Logging

The application records:

- Login Status
- Incoming Messages
- AI Responses
- Errors
- Connection Events
- Authentication Status

Logs are stored locally for debugging and monitoring.

---

# AI Capabilities

The integrated language model can:

- Understand conversation history
- Maintain context
- Detect emotional tone
- Reply naturally
- Mix English and Hindi conversationally
- Avoid repetitive responses
- Simulate real human interaction

---

# Future Improvements

- Voice Message Support
- Image Understanding
- Multi-account Management
- Dashboard Interface
- Sentiment Analytics
- Database-backed Memory
- Cloud Deployment
- Plugin Architecture
- Multi-platform Messaging
- Web Control Panel

---

# Disclaimer

This project is intended for educational, research, and automation learning purposes. Users are responsible for complying with Instagram's Terms of Service and API policies.

---

# Author

**D4RK D3V1L**

AI Developer • Python Developer • Automation Engineer • Cybersecurity Enthusiast

---

## License

MIT License
