
# [Name]
Project description

## Prerequisites
All required packages are provided in [src/requirements.txt](src/requirements.txt) and can be installed using `pip`
````sh
pip install -r src/requirements.txt
````

## Configuration
An example configuration is provided as [app.conf](app.conf).

**[Logging]** is provided to the logger configuration as keyword arguments

**[Serve]** is provided to `app.run` as keyword arguments

## Deployment
There are multiple options to deploying the app.

**Python**
````sh
python3 src/app.py
````

**Docker Container**
````sh
docker build -t [tag-name] src/

docker run -v app.conf:/app/app.conf [tag-name]
````

**Docker Compose**
````sh
docker compose up -d
````

## Debugging
The [.flaskenv](.flaskenv) configuration ensures that the app can be started from the project root using `flask run` command. This will launch the app locally in debug mode.

````sh
flask run
````