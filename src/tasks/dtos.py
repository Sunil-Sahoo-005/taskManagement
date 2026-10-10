#HERE SCHEMA WILL BE DEFINED TO HANDLE DATA IN BACKEND
from pydantic import BaseModel


class Taskschema(BaseModel):
    title :str
    description :str
    is_complete : bool =False

#AFTER COMPLETE SCHEMA CONNECT IT TO ROUTER
# BEACUSE THE DATA WILL BE RECIEVED IN ROUTER THROUGH FRONTEND