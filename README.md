## Step 0.5

run on Ubuntu VM with `python -m uvicorn web_server:app --reload --port 5045 --host 0.0.0.0` after creating a venv


## Step 1

after building the image with `docker build -t IMAGE_NAME .`, used `docker run -d --name CONTAINER_NAME -p 5045:8000 IMAGE_NAME` to run the containerized app

