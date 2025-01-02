FROM python:3.12

# set the working directory
WORKDIR /app

# install poetry
RUN pip install poetry

# copy only poetry files
COPY pyproject.toml poetry.lock ./

# export and install dependencies
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the rest of the app
COPY . /app

# start the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
