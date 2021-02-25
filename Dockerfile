FROM python:3
COPY Requirements.txt /
RUN pip install -r /Requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "server.py"]