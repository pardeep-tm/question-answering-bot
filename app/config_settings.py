"""Configuration module for the serivce"""

import os
from environs import Env
from pydantic_settings import BaseSettings


env = Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(BASE_DIR, ".app.env"))


class Settings(BaseSettings):
    """Settings class for configuration from environment variables.

    Args:
        BaseSettings (Any): Pydantic class for settings
    """

    LLM_MODEL: str = env("LLM_MODEL")
    OPENAI_API_KEY: str = env("OPENAI_API_KEY")

settings = Settings()