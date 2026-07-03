from fastapi import APIRouter, HTTPException

from app.models.request import ComposeRequest
from app.models.response import ComposeResponse
from app.services.message_service import MessageService


router = APIRouter()

message_service = MessageService()


@router.get("/")
def root():
    return {
        "message": "Merchant AI Assistant is running successfully!"
    }


@router.get("/healthz")
def health_check():
    return {
        "status": "healthy"
    }


@router.get("/metadata")
def metadata():
    return {
        "bot_name": "Merchant AI Assistant",
        "version": "1.0.0",
        "author": "Karthika",
        "framework": "FastAPI",
        "llm": "Gemini 2.5 Flash",
        "supported_languages": [
            "English",
            "Hindi",
            "Hinglish"
        ]
    }


@router.post(
    "/tick",
    response_model=ComposeResponse,
)
def compose_message(
    request: ComposeRequest,
):

    try:

        response = message_service.compose(
            merchant_id=request.merchant_id,
            trigger_id=request.trigger_id,
            customer_id=request.customer_id,
        )

        return response

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )