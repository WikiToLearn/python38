FROM python:3.5

RUN pip install pyyaml==3.12
RUN pip install requests==2.11.1

ADD ./src/ /tmp/wtl/
RUN cd /tmp/wtl/ && pip install .
