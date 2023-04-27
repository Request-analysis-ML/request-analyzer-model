FROM python:3.11

WORKDIR /app
COPY . /app

EXPOSE 8090

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]


CMD ["app.py"]