from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.models import TaskModel
from src.tasks.route import task_routes

Base.metadata.create_all(engine)

app=FastAPI(title="This is my Task-Management Application !")

#JO ROUITE CONNECT HOGI IN task_routes KE SATH AB BO AAYEGI MERE FAST API KE SERVER MAI MEANS (app)
app.include_router(task_routes)