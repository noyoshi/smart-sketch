FROM python:3.6-slim
LABEL Noah Yoshida "nyoshida@nd.edu"
RUN apt-get update -y && apt-get install -y gcc libc-dev

COPY . /app
ENV HOME=/app
WORKDIR /app
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json

RUN pip3 install -r requirements.txt
# TODO change this 
EXPOSE 5000 

ENTRYPOINT ["python3", "tornado_server/server.py"]