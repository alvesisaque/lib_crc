FROM python:3

ADD . /code

WORKDIR /code

#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
RUN pip install -r requirements.txt

#COPY . /opt/app

CMD python main.py