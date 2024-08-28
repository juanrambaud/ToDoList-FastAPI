from typing import Union
from fastapi import FastAPI, HTTPException
import os
from supabase import create_client, Client
from supabase_functions import create_supabase_client
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import date, datetime
from enum import Enum

client = create_supabase_client()

data = client.table("ToDoList").select("*").execute()
#print(type(data))


class Task(BaseModel):

    #id: None
    learn: str
    stage: str = "To Do"
    comment: str
    date: datetime = date.today()

type_stage = ["To Do", "Doing", "Done"]

#FastAPI
app = FastAPI()

#run server
# fastapi dev main.py

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/completelist/")
async def read_list():
    data = client.table("ToDoList").select("*").order("id", desc=False).execute()
    #print(type(data))
    return data

@app.get("/list/{stage_id}")
async def read_list(stage_id: str):
    data = client.table("ToDoList").select("*").eq("stage", stage_id).order("id", desc=False).execute()
    #print(type(data))
    return data


@app.post("/addtask/", status_code=201) #* cambio a un 201 como respuesta default para avisar que se creo algo.
async def add_task(task: Task):
    if task.stage in type_stage:
        json_data = jsonable_encoder(task)
        data = client.table("ToDoList").insert(json_data).execute()
        return data
    else:
        raise HTTPException(status_code=404, detail="error in the 'stage' type") #* lanzo un error de que no se pudo crear

@app.put("/updatetask/{task_id}/{stage}")
async def update_task(task_id: int, stage: str):
    json_date = jsonable_encoder(date.today())
    if stage in type_stage:
        data = client.table("ToDoList").update({"stage": stage, "date": json_date}).eq("id", task_id).execute()
        return data
    else:
        raise HTTPException(status_code=404, detail="error in the 'stage' type") #* lanzo un error de que no pudo actualizarse 
    
@app.delete("/deletetask/{task_id}", status_code=201) #* cambio a un 201 como respuesta default para avisar que se creo algo.
async def delete_task(task_id: int): 
    data = client.table("ToDoList").delete().eq("id", task_id).execute()
    print(len(data.data))
    if len(data.data) == 0: #* 404: The server cannot process the request due to syntax errors, invalid data, or other errors on the client side.
        raise HTTPException(status_code=404, detail="ID not found") 
        