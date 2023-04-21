FROM python:3.11

WORKDIR /app
COPY . /app

EXPOSE 8090

RUN pip install --upgrade pip
RUN pip install -r api_files/requirements.txt

ENTRYPOINT [ "python" ]


CMD ["api_files/app.py"]