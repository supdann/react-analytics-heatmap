import logging

logger = logging.getLogger(__name__)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# LOAD ENV VARIABLES FROM DOTENV
import dotenv
import os

dotenv.load_dotenv(".env")
APP_PORT = os.getenv("CV2_FASTAPI_PORT")

import app
from app.api import api_router, tags_metadata

# SETUP Fastapi App
app = FastAPI(
    title="CV2 Service",
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
