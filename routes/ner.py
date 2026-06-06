from fastapi import APIRouter

from schemas.ner import NERRequest
from services.ner import extract_entities

router = APIRouter(tags=["NER"])

@router.post("/ner")
def ner(request: NERRequest):
    return extract_entities(
        request.text
    )