import os
import requests

def generate_image(prompt: str):

    response = requests.post(
        "https://api.siliconflow.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {os.getenv('SILICONFLOW_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "black-forest-labs/FLUX.1-schnell",
            "prompt": prompt,
            "image_size": "1024x1024"
        }
    )

    response.raise_for_status()

    data = response.json()

    return {
        "prompt": prompt,
        "image_url": data["images"][0]["url"]
    }