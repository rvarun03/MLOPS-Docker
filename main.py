from fastapi import FastAPI
from routes.translation import router as translation_router
import uvicorn

app = FastAPI()

app.include_router(translation_router)

@app.get("/")
def home():
    return {"message": "AI Microservice Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)