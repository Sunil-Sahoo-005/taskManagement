from fastapi import APIRouter ,Depends,status
from src.tasks import controller
from src.tasks.dtos import Taskschema,TaskResponseschema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import session

#CONNECT task_route to fastapi server means import in main.py
task_routes=APIRouter(prefix="/tasks")


#JO DATA CONTROLLER RECIVE KARTA HAI WAHI DATA ROUTER BHI RECIVE KAREGA



@task_routes.post("/create",response_model=TaskResponseschema, status_code=status.HTTP_201_CREATED)



#USE DEPENDENCY INJECTION IN GET DB IT IS USE TO CREATE DB IMPORT DPENDS,IMORT GET_DB


def create_task(body:Taskschema, db:session = Depends(get_db)):
    return controller.create_task(body,db)


#NOW DB RECEIVE RECEIVE IN CONTROLLER

@task_routes.get("/getalltasks",response_model= list[TaskResponseschema],status_code=status.HTTP_200_OK)
def get_all_tasks(db:session = Depends(get_db)):
    return controller.get_all_tasks(db)

@task_routes.get("/getonetask/{task_id}",response_model=TaskResponseschema ,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int ,db:session = Depends(get_db)):
    return controller.get_one_tasks(task_id, db)

@task_routes.put("/updatetask/{task_id}",response_model=TaskResponseschema ,status_code=status.HTTP_201_CREATED)
def update_task(task_id : int , body : Taskschema ,db:session = Depends(get_db) ):
    return controller.update_task(task_id,body,db)

@task_routes.delete("/deletetask/{task_id}",response_model=None ,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id : int, db:session = Depends(get_db)):
    return controller.delete_task(task_id,db)