from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_DB_URL: str = "mongodb://localhost:27017/"
    MONGO_DB_NAME: str = "chat_data"
    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODELS: str = "phi3:mini"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
