FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip3 install ./
WORKDIR /app/app
CMD ["python3","./app.py"]