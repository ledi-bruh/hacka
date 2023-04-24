from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 9999
    docs_url: str = '/docs'
    redoc_url: str = '/redoc'
    
    db_login: str
    db_password: str
    db_host: str
    db_port: int
    db_database: str
    db_schema: str

    class Config:
        env_file = '../../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
