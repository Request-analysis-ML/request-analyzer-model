FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r api_files/requirements.txt

ENTRYPOINT [ "python" ]


CMD ["api_files/app.py"]