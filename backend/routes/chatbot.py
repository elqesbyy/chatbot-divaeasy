from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.chatbot_service import ask_chatbot

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_chatbot(request.message)

    return {
        "answer": answer
    }