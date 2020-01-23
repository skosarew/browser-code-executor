FROM ubuntu:latest

RUN apt-get update \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip
	
COPY ./browser-code-executor/ ./browser-code-executor/

WORKDIR /browser-code-executor/

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

