FROM python:3.10
WORKDIR /emoapiendpoints
COPY requirements.txt /emoapiendpoints/requirements.txt
RUN python3 -m pip install --upgrade -r /emoapiendpoints/requirements.txt
COPY . /emoapiendpoints/api
EXPOSE 8000
CMD [ "uvicorn",  "api.emoapi:app", "--host", "0.0.0.0", "--port", "8000"]
