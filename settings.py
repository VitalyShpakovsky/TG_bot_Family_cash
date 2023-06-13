# pip install python-dotenv
from dotenv import load_dotenv
import os

from pydantic import BaseSettings, SecretStr


load_dotenv()


class BotAPISettings(BaseSettings):
    token_key: SecretStr = os.getenv('TOKEN_API', None)
