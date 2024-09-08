import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

class Settings():
    DB_NAME: str
    DB_HOST: str
    DB_USER: str
    DB_PWD: str

settings = Settings()
load_dotenv(find_dotenv())
settings.DB_NAME = os.environ.get("DB_NAME")
settings.DB_HOST = os.environ.get("DB_HOST")
settings.DB_USER = os.environ.get("DB_USER")
settings.DB_PWD = os.environ.get("DB_PWD")