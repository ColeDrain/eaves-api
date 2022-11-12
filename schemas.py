from pydantic import BaseModel


class AudioBase(BaseModel):
    audio_path: str


class AudioCreate(AudioBase):
    pass


class Audio(AudioBase):
    id: int
    user_id: int
    job_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    firstname: str
    lastname: str
    company_name: str
    company_size: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    audios: list[Audio] = []

    class Config:
        orm_mode = True


class JobBase(BaseModel):
    pass


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    audio: Audio

    class Config:
        orm_mode = True


class TranscribeBase(BaseModel):
    pass


class TranscribeCreate(TranscribeBase):
    transcribe_text: str


class Transcribe(TranscribeBase):
    id: int
    job: Job

    class Config:
        orm_mode = True


class SentimentBase(BaseModel):
    positive_score: int
    negative_score: int
    neutral_score: int


class SentimentCreate(SentimentBase):
    positive_score: int
    negative_score: int
    neutral_score: int


class Sentiment(SentimentBase):
    id: int
    transcribe: Transcribe

    class Config:
        orm_mode = True
