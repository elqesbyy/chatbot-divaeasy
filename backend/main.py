from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.chatbot import router

app = FastAPI(title="DivaEasy Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Chatbot is running!"}