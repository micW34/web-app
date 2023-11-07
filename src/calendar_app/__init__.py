from .router import api
from fastapi import FastAPI

app = FastAPI()
app.mount("/api", api)