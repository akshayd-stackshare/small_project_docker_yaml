# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set the working directory in Docker
WORKDIR /app

ENV PYTHONPATH=/app/src:$PYTHONPATH
# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and dependencies
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app/
COPY . /app/

# Specify the command to run on container start
CMD ["pipenv", "run", "uvicorn", "src:api:main", "--host", "0.0.0.0", "--port", "8000"]
