FROM python:3

ADD . /lib_crc

RUN cd /lib_crc

RUN pip install requirements.txt


CMD [ "python", "./main.py" ]