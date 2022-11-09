from fastapi import FastAPI
from models import Audio, Response

description = """
Eaves API helps you analyse sentiments in your customer support calls
"""

app = FastAPI(
    title="Eaves API",
    description=description,
    version="0.0.1",
)

@app.post("/analyse", response_model=Response)
async def analyse(audio: Audio):
    result = Response()
    result.friendly_score = 34
    result.customer_satisfaction = 87
    return result
