from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    company_name = Column(String, index=True)
    company_size = Column(Integer)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    password = Column(String, index=True)

    audio_job = relationship("AudioJob", back_populates="user")

class AudioJob(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    user = relationship("User", back_populates="audios")
    audio_file =  Column(String)
    transcript = relationship("Transcribe", back_populates="audio_job")

class Transcribe(Base):
    __tablename__ = "Transcribes"

    id = Column(Integer, primary_key=True, index=True)
    transcribed_text = Column(String, index=True)
    sentiment = relationship("Sentiment", back_populates="transcribe")
    audio_job = relationship("Job", back_populates="job")

class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    friendly_score: int
    customer_satisfaction: int

    transcribe = relationship("Transcribe", back_populates="sentiment")
