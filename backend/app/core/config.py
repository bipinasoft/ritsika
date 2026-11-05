from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    APP_ENV: str = "local"
    SECRET_KEY: str = "unsafe-local-only-change-me"
    DATABASE_URL: str = "postgresql+psycopg://ritsika:change-me@localhost:5432/ritsika"
    REDIS_URL: str = "redis://localhost:6379/0"
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:5174,http://localhost:5175"
    RAZORPAY_KEY_ID: str = ""
    RAZORPAY_KEY_SECRET: str = ""
    RAZORPAY_WEBHOOK_SECRET: str = ""
    @property
    def cors_origin_list(self) -> list[str]:
        return [v.strip() for v in self.CORS_ORIGINS.split(",") if v.strip()]

settings = Settings()
