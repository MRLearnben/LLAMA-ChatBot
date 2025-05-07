from fastapi import FastAPI, Request
from pydantic import BaseModel
import ollama

app = FastAPI()
client = ollama.Client()

MODEL_NAME = "llama3.2"  # Change to your installed Llama model name

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = client.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response['message']['content']}
