from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=f"{os.path.join(os.path.dirname(__file__), '../.env')}")
BOT_TOKEN = os.getenv("BOT_TOKEN")

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(token=BOT_TOKEN))
