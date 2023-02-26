FROM python:3.10

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade -r requirements.txt
COPY . /EmoAPIEndpoints
EXPOSE 8000
CMD [ "uvicorn",  "EmoAPIEndpoints.EmoAPI:app", "--host", "0.0.0.0", "--port", "8000"]
