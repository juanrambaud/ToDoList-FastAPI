from fastapi import FastAPI
import os
from datetime import date
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from classes import Task, type_stage


#? Create client
def create_supabase_client():
    load_dotenv()  # take environment variables from .env.
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    return supabase

client = create_supabase_client()


#?login
#user = supabase.auth.sign_up({ "email": "user_email", "password": "user_password" })

#?select
#data = supabase.table("ToDoList").select("*").execute()
#data = client.table("ToDoList").select("*").order("id", desc=False).execute()
#data = client.table("ToDoList").select("*").eq("stage", stage_id).order("id", desc=False).execute()
def read_complete_list():
    response = client.table("ToDoList").select("*").order("id", desc=False).execute()
    return response.data


def read_stage_list(stage_id):
    response = client.table("ToDoList").select("*").eq("stage", stage_id).order("id", desc=False).execute()
    return response.data


#?insert
#data = supabase.table("ToDoList").insert({"learn":"PostgreSQL", "stage":"To Do", "comment":"Database noSQL"}).execute()
def insert_task(task):
    if task.stage == (type_stage.ToDo or type_stage.Doing or type_stage.Done):
        json_task = jsonable_encoder(task)
        response = client.table("ToDoList").insert(json_task).execute()
        return response.data
    else:
        raise HTTPException(status_code=404, detail="error in the 'stage' type. Try 'To Do' 'Doing' or 'Done'") #* lanzo un error de que no se pudo crear


#?update
#data = supabase.table("ToDoList").update({"stage":"Doing"}).eq("id", 1).execute()
def update_task_list(task_id, stage):
    json_date = jsonable_encoder(date.today())
    if stage in type_stage:
        response = client.table("ToDoList").update({"stage": stage, "date": json_date}).eq("id", task_id).execute()
        return response.data
    else:
        raise HTTPException(status_code=404, detail="error in the 'stage' type") #* lanzo un error de que no pudo actualizarse 

#?delete 
#data = supabase.table("ToDoList").delete().eq("id", 17).execute()
def delete_task_list(task_id):
    response = client.table("ToDoList").delete().eq("id", task_id).execute()
    if len(response.data) == 0: #* 404: The server cannot process the request due to syntax errors, invalid data, or other errors on the client side.
        raise HTTPException(status_code=404, detail="ID not found") 