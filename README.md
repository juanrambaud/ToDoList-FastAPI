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

using diferents queries un web explorer, we can consult the list and the task stage.

## Proyect technologies used:

- [Python](#python)
- [FastAPI](#fastapi)
- [Supabase](#supabase)
- [Python-env](#python-env)
- [Docker](#docker)
- [License](#license)


## Python   

[![My Skills](https://skillicons.dev/icons?i=py)](https://www.python.org/) A lenguaje for the API programming in VSCode.


## FastAPI  

[![My Skills](https://skillicons.dev/icons?i=fastapi)](https://fastapi.tiangolo.com/) Technologie to create a API

## Supabase   

[![My Skills](https://skillicons.dev/icons?i=supabase)](https://supabase.com/) Creation of type a DB with some task

![Captura de pantalla 2024-08-28 195853](https://github.com/user-attachments/assets/3de94071-1a8b-4faf-b0bf-19345762b0a9)

Then Created and enabling policies from DB because if this is not the case, nothing can be done from the API. :triangular_flag_on_post:

![Captura de pantalla 2024-08-28 195923](https://github.com/user-attachments/assets/74e6f3b0-1531-447d-bef1-ec9dac1c0bb5)

For last copy and past our API KEYs into a .env file

![Captura de pantalla 2024-08-28 200118](https://github.com/user-attachments/assets/d41312c0-b1be-445a-b140-4330d3775da4)


## Python-env 
⚙️ Python-env for use a creation of "enviroment variables" for use KEY in a supabase DB. :warning:

![Captura de pantalla 2024-08-28 210215](https://github.com/user-attachments/assets/e191b37b-6fed-4a72-88fb-1f125be52e8f)

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

![Captura de pantalla 2024-09-01 163438](https://github.com/user-attachments/assets/f9009c70-609c-4476-81b6-fb25aea52ba2)

Then create a container, included enviroments variables for supabase.
![Captura de pantalla 2024-09-01 163451](https://github.com/user-attachments/assets/ef4ff72f-166b-455c-80a6-917e183b4aad)

Then check in logs if it's work localy
![Captura de pantalla 2024-09-01 164428](https://github.com/user-attachments/assets/96b02a41-32e7-40db-a0de-3a89b8fc997b)
![Captura de pantalla 2024-09-01 164741](https://github.com/user-attachments/assets/2ad2c59d-0cef-4112-a728-6e4c12af689d)


4. To push the image, use the docker push command. Be sure to replace DOCKER_USERNAME with your username:
```sh
docker push <DOCKER_USERNAME>/<APP_NAME> .
```
![Captura de pantalla 2024-09-01 163757](https://github.com/user-attachments/assets/017d661f-dc26-4472-89c5-865a849bd396)










For Last i deploy the image in [Render.com](https://render.com/) and check if the API works.

Using directly a web browser.

![Captura de pantalla 2024-08-30 194946](https://github.com/user-attachments/assets/53b46f51-a2ee-41a0-a421-cdbe6a927a9a)


Using a thunder client on VSCode.

![Captura de pantalla 2024-08-30 195004](https://github.com/user-attachments/assets/91cf9cda-5e0c-4b2f-b586-88a2e79378de)


## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





