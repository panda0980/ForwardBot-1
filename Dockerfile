FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y

RUN pip install --upgrade pip

RUN pip3 install -U pip




WORKDIR /app/
COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["python3 -m forwardbot"]
