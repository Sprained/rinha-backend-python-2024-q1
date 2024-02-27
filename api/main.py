import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from endpoints.client import router

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s"
)

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)