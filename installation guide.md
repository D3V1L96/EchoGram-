# Installation Guide

Thank you for choosing **EchoGram AI**.

This guide will help you install, configure, and run the application correctly. Please follow each step in order.

---

# Prerequisites

Before installing EchoGram AI, make sure your system meets the following requirements.

| Requirement | Details |
|------------|---------|
| Operating System | Windows 10/11 (Recommended) |
| Python | Version 3.10 or later |
| Internet Connection | Required |
| Instagram Account | Required |
| Groq API Key | Required |

---

# Step 1 — Download the Project

Download the latest release from GitHub.

```bash
git clone https://github.com/D3V1L96/EchoGram-AI.git

cd EchoGram-AI
```

Or download the ZIP file and extract it.

---

# Step 2 — Create a Virtual Environment (Recommended)

Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3 — Install Required Packages

Install all required dependencies.

```bash
pip install -r requirements.txt
```

Wait until the installation completes successfully.

---

# Step 4 — Configure Your Groq API Key

Open the main project file and locate:

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Replace it with your own API key.

You can create a free API key from:

https://console.groq.com/

---

# Step 5 — Set an Application Password

Locate:

```python
correct_password = "your_password"
```

Replace it with a secure password of your choice.

This password is required every time the application starts.

---

# Step 6 — Start EchoGram AI

Run the application.

```bash
python main.py
```

---

# Step 7 — Authenticate Your Instagram Account

The first time you run EchoGram AI:

1. Log into your Instagram account using your browser.
2. Copy your **SessionID** cookie.
3. Paste the SessionID into the terminal when prompted.
4. EchoGram AI will verify your account.
5. Your session will be securely saved for future use.

You only need to do this once unless your Instagram session expires.

---

# Successful Installation

If everything is configured correctly, you should see:

- Application banner
- Password prompt
- Session loaded successfully
- Connected to Instagram
- Connected to Groq AI
- "Listening..." message

The application is now ready to automatically respond to incoming Instagram messages.

---

# Updating the Application

To update EchoGram AI:

```bash
git pull

pip install -r requirements.txt
```

---

# Common Issues

## Missing Python Package

```bash
pip install <package_name>
```

Example:

```bash
pip install aiograpi
```

---

## Invalid API Key

Verify that:

- Your Groq API key is correct.
- The API key is active.
- Your internet connection is working.

---

## Instagram Login Failed

Delete the saved session file:

```
instagram_session.json
```

Restart the application and authenticate again.

---

## Session Expired

Remove the existing session file:

```
instagram_session.json
```

Launch the application again and enter a new SessionID.

---

# Security Recommendations

- Never share your Groq API key.
- Never upload `instagram_session.json` to GitHub.
- Keep your application password private.
- Add sensitive files to `.gitignore`.
- Regularly update your dependencies.

---

# Need Help?

If you encounter any issues:

1. Verify that all installation steps were completed.
2. Check the application log for errors.
3. Ensure your API key and SessionID are valid.
4. Open an issue on the GitHub repository if the problem persists.

---

## Developer

**D4RK D3V1L**

GitHub: https://github.com/D3V1L96

Thank you for using **EchoGram AI**. Your support and feedback help improve the project.
