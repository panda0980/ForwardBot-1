FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y

RUN pip install --upgrade pip

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt



WORKDIR /app/
COPY . /app/

CMD ["python3 -m forwardbot"]
