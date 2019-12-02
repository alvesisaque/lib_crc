FROM python:3

#ADD . /lib_crc

#RUN cd /lib_crc

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY . /opt/app

CMD [ "python", "./main.py" ]