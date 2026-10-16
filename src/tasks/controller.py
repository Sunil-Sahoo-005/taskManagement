#ALL LOGIC ARE HERE 
from src.tasks.dtos import Taskschema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

#AFTER COMPLETE LOGIC CONNECT TO ROUTE
def create_task(body:Taskschema , db:Session,):
    #check
    # print(body.model_dump())
    data=body.model_dump()
    #NOW I WANT A OBJECT FROM MODEL CLASS WHICH NAME IS TASKMODEL
    #ISSE TASKMODEL NAAM KA OBJECT BANEGA JO KI NEW_TASK MAI RAHEGA     
    new_task= TaskModel( title = data["title"],
                        description = data["description"],
                        is_complete = data["is_complete"]

    )
    # NOW I WANT DB WHICH WILL HELP ME TO CONNECT WITH DATABASE DB.PY MAI GETDB FUNCTION HAI

    #MODEL DUMP() IS A METHOD IN PYDENTIC CLASS JO PYDENTIC CLASS KA OBJECT KO DICTIONARY MAI CONVERT KAR DEGI


    #store in DB
    db.add(new_task)
    db.commit()
    #COMMIT PE JO BHI DATA AAYEG WO TABLE PAI STORE HO JAYEGA
    db.refresh(new_task)
    return new_task
# {"status":"Task Created Successfully!","MSG":new_task}


def get_all_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return tasks
# {
#         "msg":"fetched all tasks",
#         "data":tasks
#     }



def get_one_tasks(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)

    if not one_task:
        raise HTTPException(
            status_code=404,
            detail="Task id not found"
        )

    return one_task
# {
#         "status": "data fetched successfully",
#         "data": one_task
#     }


def update_task( task_id: int , body : Taskschema ,db:Session):
    one_task = db.query(TaskModel).get(task_id)

    if not one_task:
            raise HTTPException(
                status_code=404,
                detail="Task id not found"
            )
    
    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_complete = body.is_complete

    #shortcut for manual
    body = body.model_dump()
    for key , value in body.items():
         setattr(one_task , key , value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return {
            "status": "data updated successfully",
            "data": one_task
        }

def delete_task(task_id: int , db:Session):
     one_task=db.query(TaskModel).get(task_id)

     if not  one_task:
          raise HTTPException(
               status_code=404,
               detail="Task id not found"
          )
     db.delete(one_task)
     db.commit()

     return None
# {
#                  "status": "data deleted successfully",
#                  "data": one_task
#              }