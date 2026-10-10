from fastapi import APIRouter ,Depends
from src.tasks import controller
from src.tasks.dtos import Taskschema
from src.utils.db import get_db

#CONNECT task_route to fastapi server means import in main.py
task_routes=APIRouter(prefix="/tasks")


#JO DATA CONTROLLER RECIVE KARTA HAI WAHI DATA ROUTER BHI RECIVE KAREGA
@task_routes.post("/create")\
#USE DEPENDENCY INJECTION IN GET DB IT IS USE TO CREATE DB IMPORT DPENDS,IMORT GET_DB
def create_task(body:Taskschema, db = Depends(get_db)):
    return controller.create_task(body,db)
#NOW DB RECEIVE RECEIVE IN CONTROLLER

@task_routes.get("/getalltasks")
def get_all_tasks(db = Depends(get_db)):
    return controller.get_all_tasks(db)

@task_routes.get("/getonetask/{task_id}")
def get_one_task(task_id:int ,db = Depends(get_db)):
    return controller.get_one_tasks(task_id, db)