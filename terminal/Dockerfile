FROM python:3.8

WORKDIR /app
COPY . .

run pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]