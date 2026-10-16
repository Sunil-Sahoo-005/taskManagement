#HERE SCHEMA WILL BE DEFINED TO HANDLE DATA IN BACKEND
from pydantic import BaseModel


class Taskschema(BaseModel):
    title :str
    description :str
    is_complete : bool =False

#AFTER COMPLETE SCHEMA CONNECT IT TO ROUTER
# BEACUSE THE DATA WILL BE RECIEVED IN ROUTER THROUGH FRONTEND


# FOR JWT AUTH TOKEN WE USE THIS MODEL TO CUSTOMJZE WHILL DATA I WANT TO RETURN OR NOT

class TaskResponseschema(BaseModel):
    id : int
    title :str
    description :str
    # is_complete : bool =False