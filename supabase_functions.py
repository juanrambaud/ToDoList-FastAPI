import os
from supabase import create_client, Client
from dotenv import load_dotenv
from dotenv import load_dotenv


def create_supabase_client():
#cargo los datos y creo el cliente supabase
    load_dotenv()  # take environment variables from .env.
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    return supabase


#login
#user = supabase.auth.sign_up({ "email": "jmrambaud88@gmail.com", "password": "Juansupabase1!" })
#print(user)

#query
#data = supabase.table("ToDoList").select("*").execute()
#print("que traje:")
#print(data)
#data = client.table("ToDoList").select("*").order("id", desc=False).execute()

#insert
#data = supabase.table("ToDoList").insert({"learn":"PostgreSQL", "stage":"To Do", "comment":"Database noSQL"}).execute()

#update
#data = supabase.table("ToDoList").update({"stage":"Doing"}).eq("id", 1).execute()

#delete
#data = supabase.table("ToDoList").delete().eq("id", 17).execute()