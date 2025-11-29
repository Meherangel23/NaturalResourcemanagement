from fastapi import APIRouter
from ..models import schemas
from .. import llm

router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)

@router.post("/message")
async def chat(message: schemas.ChatMessage):
    prompt = f"You are a helpful assistant for a natural resource management company. A user is asking: '{message.text}'. Provide a helpful and concise response."
    response_text = llm.get_chatbot_reply(prompt)
    return {"reply": response_text}