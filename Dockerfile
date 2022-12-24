FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y

RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY ./ /app/

RUN pip install --upgrade pip


WORKDIR /app/
CMD ["python3 -m forwardbot"]
