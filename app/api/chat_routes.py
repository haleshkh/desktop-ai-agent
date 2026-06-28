from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.graph.desktop_graph import desktop_graph

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = desktop_graph.invoke(
        {
            "query": request.query
        }
    )

    print("RESULT= ", result) 
    return result  # <-- Add this line

    
    