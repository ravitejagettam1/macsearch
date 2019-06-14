FROM python:3

ADD Mac_search.py /
COPY requirements.txt /

RUN pip3 install --upgrade-strategy only-if-needed -r requirements.txt

#CMD ["python","./Mac_search.py"]

ENTRYPOINT ["python","./Mac_search.py"]

