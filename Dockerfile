FROM python:3.9-slim
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b :8080", "main:app", "--access-file -", "--capture-output"]