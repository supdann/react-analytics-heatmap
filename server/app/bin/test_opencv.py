# LOAD ENV VARIABLES USING DOTENV
import dotenv
dotenv.load_dotenv(".env")

# APP
from app.main import app
import os

APP_PORT = int(os.getenv("APP_PORT"))

def run():
    print("it works")
