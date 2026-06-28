#  Desktop AI Agent

An AI-powered Desktop Assistant built using **FastAPI**, **LangGraph**, and **Google Gemini**. The application understands natural language commands and performs desktop automation such as opening applications, opening websites, and creating folders. It can also be controlled remotely from a mobile phone using **Cloudflare Tunnel**.

---

##  Features

*  Create folders using natural language
*  Open Google
*  Open YouTube
*  Open Visual Studio Code
*  Open GitHub
*  AI-based request routing using Google Gemini
*  Multi-Agent Architecture with LangGraph
*  Remote access from anywhere using Cloudflare Tunnel
* Web interface built with HTML, CSS, and JavaScript

---

##  Project Architecture

```
Phone
   │
   ▼
Cloudflare Tunnel
   │
   ▼
FastAPI Backend
   │
   ▼
LangGraph
   │
   ▼
Manager Agent (Gemini)
   │
 ┌──────────────┐
 ▼              ▼
Browser Agent   File Agent
 │              │
 ▼              ▼
Browser       Windows File System
```

---

##  Technologies Used

* Python
* FastAPI
* LangGraph
* LangChain
* Google Gemini API
* HTML
* CSS
* JavaScript
* Cloudflare Tunnel
* Git & GitHub

---

##  Project Structure

```
desktop-ai-agent/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── graph/
│   ├── llm/
│   ├── schemas/
│   ├── static/
│   ├── templates/
│   ├── tools/
│   └── main.py
│
├── workspace/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/haleshkh/desktop-ai-agent.git
```

Move into the project:

```bash
cd desktop-ai-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

##  Remote Access

This project supports remote access using **Cloudflare Tunnel**.

Run:

```bash
cloudflared tunnel --url http://localhost:8000
```

Open the generated URL on your phone and control your laptop remotely.

---

##  Future Improvements

* Voice Commands
* Terminal Agent
* PDF Reader Agent
* Email Agent
* Authentication
* Conversation Memory
* Multi-Step AI Planning

---

##  Author

**Halesh K H**

GitHub: https://github.com/haleshkh
