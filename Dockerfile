FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /abis
WORKDIR /abis
ADD requirements.txt /abis
RUN pip install -r requirements.txt
ADD . /abis/
