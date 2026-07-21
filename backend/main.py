from fastapi import FastAPI
from routes.chatbot import router

app = FastAPI(title="DivaEasy Chatbot")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Chatbot API is running"}