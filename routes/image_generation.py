from fastapi import APIRouter

from schemas.image_generation import ImageGenerationRequest
from services.image_generation_service import generate_image

router= APIRouter(tags=["Image Generation"])

@router.post("/generate-image")
def image_generation(request: ImageGenerationRequest):
    return generate_image(request.prompt)

