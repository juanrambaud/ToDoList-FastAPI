from typing import Union
from fastapi import FastAPI
import os
from supabase import create_client, Client
from supabase_usage import create_supabase_client


client = create_supabase_client()

data = client.table("ToDoList").select("*").execute()
#print(type(data))

#FastAPI
app = FastAPI()

#run server
# fastapi dev main.py

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/completelist")
def read_list():
    data = client.table("ToDoList").select("*").order("id", desc=False).execute()
    print(type(data))
    return data

@app.get("/list/{stage_id}")
def read_list(stage_id: str):
    data = client.table("ToDoList").select("*").eq("stage", stage_id).order("id", desc=False).execute()
    #print(type(data))
    return data
