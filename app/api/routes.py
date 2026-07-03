from fastapi import APIRouter, HTTPException

from app.models.request import ComposeRequest
from app.models.response import ComposeResponse
from app.services.message_service import MessageService
from app.models.tick_request import TickRequest
from app.models.tick_response import TickResponse
import traceback


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


@router.post("/tick", response_model=TickResponse)
def tick(request: TickRequest):

    try:

        return message_service.compose(
            merchant_id=request.merchant_id,
            trigger_id=request.trigger_id,
            customer_id=request.customer_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )