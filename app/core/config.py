# -*- coding: utf-8 -*-
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "resume_job_db")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings() 