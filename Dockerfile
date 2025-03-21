# start with slim python image
FROM python:3.11-slim

# set the working directory in the container
WORKDIR /prepapi

# copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock ./

# install dependencies
RUN pip install poetry && poetry install  --no-root

# copy the content of the local src directory to the working directory
COPY prepapi/ ./prepapi
COPY tests/ ./tests

# expose the port 8000
EXPOSE 8000

# command to run on container start
CMD ["poetry","run","uvicorn", "prepapi.main:app", "--host","0.0.0.0","--port","8000"]