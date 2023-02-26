FROM python:3.10

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade -r requirements.txt
COPY . ./emoapiendpoints
EXPOSE 8000
CMD [ "uvicorn",  "emoapiendpoints.emoapi:app", "--host", "0.0.0.0", "--port", "8000"]
