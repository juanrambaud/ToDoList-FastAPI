<p align="center">
  <a href="https://github.com/juanrambaud">
    <img src="https://skillicons.dev/icons?i=vscode,py,fastapi,supabase,docker,git" />
  </a>
</p>


# 🚀 To Do List

An app "To Do List".
The project contemplates the creation of a DB in Supabase, then the creation of an API using FastAPI.
The API consists in a list of tasks, wich can be created, updated and deleted, usign their `stage` property, for example "To Do".
The list of tasks is stored in a Supabse DB and accessed by the API created in FastAPI.

Using different queries in a web browser, we can consult the list and the task's stage.

:triangular_flag_on_post: Actually the API is not public, but you can create your own API. :triangular_flag_on_post:	

## Project technologies used:

- [Python](#python)
- [FastAPI](#fastapi)
- [Python-env](#python-env)
- [Supabase](#supabase)
- [Docker](#docker)
- [Deploy](#deploy)
- [License](#license)



## Python   

[![My Skills](https://skillicons.dev/icons?i=py)](https://www.python.org/) The API is written in Python and I used VSCode as my IDE.


## FastAPI  

[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://fastapi.tiangolo.com/) Framework to create the API.

This tutorial is not intended to explain how FastApi works, it's only to sample an implementation of this framework. In a nutshell, there are a series of HTTP methods: GET, POST, PUT and DELETE to create, update and delete a task. Plus, it's possible to get a list of tasks or to list by stage (e.g. **To Do**, **Doing** and **Done**). 

- Create a task: include a NAME, by default its stage is **To Do**; then a COMMENT, and optionally DATE. By default, `in Supabase adding a ID of task and TIMESTAMP in case that you not complete date` <- esto quiere decir que Supabase le agrega el ID por defecto?.
- Update a task: change the stage of a task, using its ID.
- Detele task: select an ID and delete the task.
- Get list: retrieve a full list of tasks or filter by stage.
  
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-11 150959](https://github.com/user-attachments/assets/fab59662-97c6-4e6a-8e6f-44181fc66306)

&nbsp;
&nbsp;


## Python-env 
⚙️ Python-env `for use a creation of "enviroment variables" for use KEY in a supabase DB.` <- no entendi esto, puede ser algo como `to create all environment variables for the Supabase DB.` quizas? :warning:
&nbsp;

You need to create an `.env` file in the project folder and add the variables (copy your variables from Supabase. In Projects Settings/API)
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 210215](https://github.com/user-attachments/assets/e191b37b-6fed-4a72-88fb-1f125be52e8f)
&nbsp;
&nbsp;


## Supabase   

[![My Skills](https://skillicons.dev/icons?i=supabase)](https://supabase.com/) To create a DB and store some tasks
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 195853](https://github.com/user-attachments/assets/3de94071-1a8b-4faf-b0bf-19345762b0a9)
&nbsp;
&nbsp;

Then create and enable policies from DB, otherwise nothing can be done from the API. :triangular_flag_on_post:
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 195923](https://github.com/user-attachments/assets/74e6f3b0-1531-447d-bef1-ec9dac1c0bb5)
&nbsp;
&nbsp;

Lastly copy and paste your API KEYs into an `.env` file. The variables are in "Projects Settings" / "API"
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 200118](https://github.com/user-attachments/assets/d41312c0-b1be-445a-b140-4330d3775da4)
&nbsp;
&nbsp;


## Docker   

[![My Skills](https://skillicons.dev/icons?i=docker)](https://www.docker.com/) I created a Docker image in the same repository to run this API. Then created a `.dockerignore` to avoid adding unwanted/secret files to the final image.

1. Build image
```sh
docker build -t <DOCKER_USERNAME>/<APP_NAME> .
```
2. To verify the image exists locally, you can use the "docker image ls" command:
```sh
docker image ls
```

Terminal returns
```sh
REPOSITORY                          TAG       IMAGE ID       CREATED          SIZE
<DOCKER_USERNAME>/<APP_NAME>        latest    1543656c9290   1 minute ago     1.12GB
...
```

Before pushing the image, I check if it works fine in my Docker Desktop, to ensure the image is created correctly and runs in local.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163438](https://github.com/user-attachments/assets/f9009c70-609c-4476-81b6-fb25aea52ba2)
&nbsp;
&nbsp;

Then create a container, including the required enviroments variables for Supabase.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163451](https://github.com/user-attachments/assets/ef4ff72f-166b-455c-80a6-917e183b4aad)
&nbsp;
&nbsp;

Then check in logs if it works locally
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 164428](https://github.com/user-attachments/assets/96b02a41-32e7-40db-a0de-3a89b8fc997b)
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 164741](https://github.com/user-attachments/assets/2ad2c59d-0cef-4112-a728-6e4c12af689d)
&nbsp;
&nbsp;


4. To push the image, use the `docker push` command. Be sure to replace DOCKER_USERNAME with your username:
```sh
docker push <DOCKER_USERNAME>/<APP_NAME> .
```
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163757](https://github.com/user-attachments/assets/017d661f-dc26-4472-89c5-865a849bd396)
&nbsp;
&nbsp;


## Deploy
Lastly, I deploy the image in [Render.com](https://render.com/) and check if the API works.
&nbsp;
&nbsp;

1. First select a NEW/Web Services. In options I use existing image using mi Docker image
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 165315](https://github.com/user-attachments/assets/d457bc55-ee6d-42f6-a41a-cb0424ed748b)
&nbsp;
&nbsp;

3. Add enviroments variables
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 165627](https://github.com/user-attachments/assets/38ef36e4-b2d4-4a88-80ad-58a7cc2cf445)
IMPORTANT: ADD variables `KEY=PORT` and `VALUE=8000`. This is to expose port 8000, which is the default for FastAPI.
&nbsp;
&nbsp;

4. Check in log if API is deployed.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 170707](https://github.com/user-attachments/assets/b4f9f894-b265-406d-8ea3-d94b9189ec41)
&nbsp;
&nbsp;

5. Check in a web browser.\
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-30 194946](https://github.com/user-attachments/assets/53b46f51-a2ee-41a0-a421-cdbe6a927a9a)
&nbsp;
&nbsp;

Using a thunder client on VSCode.\
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-30 195004](https://github.com/user-attachments/assets/91cf9cda-5e0c-4b2f-b586-88a2e79378de)
&nbsp;
&nbsp;

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





