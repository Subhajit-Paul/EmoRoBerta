FROM python:3.10
WORKDIR /emoapiendpoints
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade -r ./requirements.txt
COPY . ./api/
EXPOSE 8000
CMD [ "uvicorn",  "api.emoapi:app", "--host", "0.0.0.0", "--port", "8000"]
