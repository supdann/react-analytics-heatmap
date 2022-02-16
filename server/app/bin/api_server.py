# LOAD ENV VARIABLES USING DOTENV
import dotenv
dotenv.load_dotenv(".env")

# APP
import uvicorn
from app.main import app
import os

APP_PORT = int(os.getenv("APP_PORT"))

def run():
    uvicorn.run(app, host='127.0.0.1', port=APP_PORT)

if __name__ == '__main__':
    run()
