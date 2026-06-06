from fastapi import APIRouter
from fastapi.responses import FileResponse

from schemas.speech import SpeechRequest
from services.speech_service import text_to_speech

router= APIRouter(tags=["Speech"])

@router.post("/speech")
def speech(request:SpeechRequest):

    filename=text_to_speech(request.text)
    
    return FileResponse(
        filename,
        media_type="audio/mpeg",
        filename=filename
    )