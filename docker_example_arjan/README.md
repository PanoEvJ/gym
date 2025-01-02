Following the docker tutorial by Arjan_Codes presented [here](https://www.youtube.com/watch?v=zkMRWDQV4Tg&list=PLC0nd42SBTaO3aajVi2FomC86q6TeRM_Y&t=209s).

Official code given [here](https://github.com/ArjanCodes/2022-docker).

## Install Dependendies

Poetry is used to manage & install the python packages. Use `poetry install --no-root` to create the python env.


## How to Serve the App Locally
Here are two ways to serve the app locally. The app will be served on:

- http://localhost:8080/  

- http://localhost:8080/channels/jackherrington (or any other channel id from the database (channels.json))

- any other route included in the `app.py`

### Option 1: Build Image & Run Container

First, build the image and then run it inside the container. This code needs to be repeated for. every code change.

Build the image:

`docker build -t channel-api .`

Run the container:

`docker run -d -p 8080:80 channel-api`

### Option 2: Compose
Use `docker compose` 

## Ports

Ports `80` & `8080` need to be available to run the container.

To check if & which processed a port is currently in use

`sudo lsof -i :<port_id>` 

To stop the use of a specific port:

`docker kill <port_id>`

To check which docker container runs on port `8080`:

`docker ps | grep 8080`

To remove an image:

`docker rmi -f <image_id>`