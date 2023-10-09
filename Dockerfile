# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set the working directory in Docker
WORKDIR /app

ENV PYTHONPATH=/app/src:$PYTHONPATH
# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and dependencies
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile && \
    pipenv run playwright install && \
    pipenv run playwright install-deps

# Copy the current directory contents into the container at /app/
COPY . /app/

EXPOSE 8001


# Specify the command to run on container start
#CMD ["/bin/bash"]
CMD ["pipenv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]
