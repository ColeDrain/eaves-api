from pydantic import BaseModel

class User(BaseModel):
    user_id: int

class Audio(BaseModel):
    audio_id: int
    audio_file: bytes
    agent_name: str

class Job(BaseModel):
    job_id: int
    audio_id: int

class Transcribe(BaseModel):
    job_id: int
    transcript: str

class Response(BaseModel):
    job_id: int
    friendly_score: int
    customer_satisfaction: int

class Sentiment(BaseModel):
    transcript_id: int
    response: Response
