This README is rough notes of key meaningful steps that were taken at each level of the mini-project.


## Level 0.5

ran on Ubuntu VM with `python -m uvicorn web_server:app --reload --port 5045 --host 0.0.0.0` after creating a venv


## Level 1

after building the image with `docker build -t IMAGE_NAME .`, used `docker run -d --name CONTAINER_NAME -p 5045:8000 IMAGE_NAME` to run the containerized app


## Level 2

Nothing significant noted

## Level 3

See `.github/workflows/docker-deploy.yml`


## Level 4

Imported a T5 model from huggingFace, splitted the existing endpoints by adding prefixes `house` and `nlp` to differentiate between the two models and added a `summarize` endpoint to give a usage exemple of the T5 model.

