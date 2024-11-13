from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_BUCKET_NAME: str

    MONGO_DB_URI: str = "mongodb://localhost:27017"
    model_config = SettingsConfigDict(env_file=(".env", ".env.prod"))


settings = Settings()
