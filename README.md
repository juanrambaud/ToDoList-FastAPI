<p align="center">
  <a href="https://github.com/juanrambaud">
    <img src="https://skillicons.dev/icons?i=vscode,py,fastapi,supabase,docker,git" />
  </a>
</p>


# 🚀 To Do List

A app "To Do List".
The proyect contemplate a creation of DB in Supabase, then a creation of API with FastAPI for query.
The API consist in a list of task, wich can created, updated and deleted, usign the "stages" in task, for example "To Do".
The List it's storage in a supabse DB and access by the API created in FastAPI

Using diferents queries in web explorer, we can consult the list and the task stage.

:triangular_flag_on_post: Actually the API it's suspended for traffic, but you can create your ouw API. :triangular_flag_on_post:	

## Proyect technologies used:

- [Python](#python)
- [FastAPI](#fastapi)
- [Python-env](#python-env)
- [Supabase](#supabase)
- [Docker](#docker)
- [Deploy](#deploy)
- [License](#license)



## Python   

[![My Skills](https://skillicons.dev/icons?i=py)](https://www.python.org/) A lenguaje for the API programming in VSCode.


## FastAPI  

[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://fastapi.tiangolo.com/) Technologie to create a API

This tutorial it's not to explain how FastApi work, it's only implement this technologie. To resume in the code are a series HTTP methods: GET, POST, PUT and DELTE to create a task, update and delete. Plus, it's  posible get a list of total task or get a list by type of task (To Do, Doing and Done). 

- Create a task: include a NAME, by default the STAGE it's To Do, a COMMENT, and optional DATE. By default, in SUPABASE adding a ID of task and TIMESTAMP in case that you not complete date.
- Update a task: change the stage of, only by your ID.
- Detele task: select an ID and delete.
- Get List: select complete list or list by STAGE type.
  
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-11 150959](https://github.com/user-attachments/assets/fab59662-97c6-4e6a-8e6f-44181fc66306)

&nbsp;
&nbsp;


## Python-env 
⚙️ Python-env for use a creation of "enviroment variables" for use KEY in a supabase DB. :warning:
&nbsp;

You need to create a .env file in the proyect folder and add the variables (copy your variables from SUPABASE. In Proyects Settings/API)
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 210215](https://github.com/user-attachments/assets/e191b37b-6fed-4a72-88fb-1f125be52e8f)
&nbsp;
&nbsp;


## Supabase   

[![My Skills](https://skillicons.dev/icons?i=supabase)](https://supabase.com/) Creation of type a DB with some task
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 195853](https://github.com/user-attachments/assets/3de94071-1a8b-4faf-b0bf-19345762b0a9)
&nbsp;
&nbsp;

Then Created and enabling policies from DB because if this is not the case, nothing can be done from the API. :triangular_flag_on_post:
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 195923](https://github.com/user-attachments/assets/74e6f3b0-1531-447d-bef1-ec9dac1c0bb5)
&nbsp;
&nbsp;

For last copy and past our API KEYs into a .env file. The variables are in "Proyects Settings" / "API"
&nbsp;
&nbsp;

![Captura de pantalla 2024-08-28 200118](https://github.com/user-attachments/assets/d41312c0-b1be-445a-b140-4330d3775da4)
&nbsp;
&nbsp;


## Docker   

[![My Skills](https://skillicons.dev/icons?i=docker)](https://www.docker.com/) I created a docker image in the same repository for APP. Then create a .dockerignore for files to ignore in the docker image.

1. Build image
```sh
docker build -t <DOCKER_USERNAME>/<APP_NAME> .
```
2. To verify the image exists locally, you can use the "docker image ls" command:
```sh
docker image ls
```

Terminal return
```sh
REPOSITORY                          TAG       IMAGE ID       CREATED          SIZE
<DOCKER_USERNAME>/<APP_NAME>        latest    1543656c9290   1 minute ago     1.12GB
...
```

Before to push the image, i check if working fine in Docker Desktop, to ensure the image it's create correctly and work in local.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163438](https://github.com/user-attachments/assets/f9009c70-609c-4476-81b6-fb25aea52ba2)
&nbsp;
&nbsp;

Then create a container, included enviroments variables for supabase.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163451](https://github.com/user-attachments/assets/ef4ff72f-166b-455c-80a6-917e183b4aad)
&nbsp;
&nbsp;

Then check in logs if it's work localy
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 164428](https://github.com/user-attachments/assets/96b02a41-32e7-40db-a0de-3a89b8fc997b)
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 164741](https://github.com/user-attachments/assets/2ad2c59d-0cef-4112-a728-6e4c12af689d)
&nbsp;
&nbsp;


4. To push the image, use the docker push command. Be sure to replace DOCKER_USERNAME with your username:
```sh
docker push <DOCKER_USERNAME>/<APP_NAME> .
```
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 163757](https://github.com/user-attachments/assets/017d661f-dc26-4472-89c5-865a849bd396)
&nbsp;
&nbsp;


## Deploy
For Last i deploy the image in [Render.com](https://render.com/) and check if the API works.
&nbsp;
&nbsp;

1. First select a NEW/Web Services. In options i use existingimage using mi Dockerimage created
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 165315](https://github.com/user-attachments/assets/d457bc55-ee6d-42f6-a41a-cb0424ed748b)
&nbsp;
&nbsp;

3. Add enviroments variables
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 165627](https://github.com/user-attachments/assets/38ef36e4-b2d4-4a88-80ad-58a7cc2cf445)
IMPORTANT: ADD variable KEY=PORT and VALUE=8000. This is for expose this port and 8000 it's the value default for FastAPI.
&nbsp;
&nbsp;

4. Check in log it's API are deploy.
&nbsp;
&nbsp;

![Captura de pantalla 2024-09-01 170707](https://github.com/user-attachments/assets/b4f9f894-b265-406d-8ea3-d94b9189ec41)
&nbsp;
&nbsp;

5. Check in web.\
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





