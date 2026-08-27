from fastapi import APIRouter
from pydantic import BaseModel

from app.llm import chat

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_api(request: ChatRequest):
    response = await chat(request.message)
    return {"response": response}