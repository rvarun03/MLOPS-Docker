from fastapi import APIRouter
from schemas.translation import TranslationRequest
from services.translation_service import translate_text

router = APIRouter(tags=["Translation"])

@router.post("/translate")
def translate(request: TranslationRequest):
    return translate_text(
        request.text,
        request.target_language
    )