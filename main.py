from fastapi import FastAPI
from supabase_functions import read_complete_list, read_stage_list, insert_task, update_task_list, delete_task_list
from classes import Task, type_stage


#FastAPI
app = FastAPI()

#run server
# fastapi dev main.py

@app.get("/")
async def read_root():
    return {"FastAPI": "working"}

@app.get("/completelist/")
async def read_list():
    response = read_complete_list()
    return response

@app.get("/list/{stage_id}")
async def read_list_type(stage_id: type_stage):
    response = read_stage_list(stage_id)
    return response

@app.post("/addtask/", status_code=201) #* cambio a un 201 como respuesta default para avisar que se creo algo.
async def add_task(task: Task):
    response = insert_task(task)
    return response

@app.put("/updatetask/{task_id}/{stage}")
async def update_task(task_id: int, stage: type_stage):
    response = update_task_list(task_id, stage)
    return response
 
@app.delete("/deletetask/{task_id}", status_code=201) #* cambio a un 201 como respuesta default para avisar que se creo algo.
async def delete_task(task_id: int): 
    response = delete_task_list(task_id)
    return response