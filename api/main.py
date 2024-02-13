import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)