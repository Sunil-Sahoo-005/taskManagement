from fastapi import FastAPI
from src.utils.db import Base,engine

app=FastAPI(title="This is my Task-Management Application !")
