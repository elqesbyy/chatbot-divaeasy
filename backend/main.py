from fastapi import FastAPI
from backend.routes.chatbot import router

app = FastAPI(
    title="DivaEasy Chatbot API"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Chatbot is running!"}