**#  WhatsApp Chatbot with Flask + LLaMA (Ollama)

This project builds a simple RESTful chatbot service in Python using:

- 🧠 LLaMA 2 via [Ollama](https://ollama.com/)
- 📲 WhatsApp via Twilio
- 🔥 Flask for the web API

---

## 💻 Features

- Accepts messages from WhatsApp
- Sends the input to LLaMA via Ollama API
- Returns AI-generated response back to WhatsApp

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt


## Connect to Twilio WhatsApp
Create a Twilio account

Configure your Webhook URL to point to:
https://218a-2401-4900-22ca-207b-9564-cf5f-162e-4a8f.ngrok-free.app/sms

Start chatting from WhatsApp!
