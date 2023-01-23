FROM python:3.11

RUN mkdir -p /usr/src/japortscan
WORKDIR /usr/src/japortscan

COPY ./JAPortScan.py /usr/src/japortscan

CMD ['python', 'japortscan.py']