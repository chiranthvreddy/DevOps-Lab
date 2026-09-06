FROM python:3.12-slim
RUN pip install --no-cache-dir "Flask>=3,<4"
WORKDIR /app
COPY app.py .
USER 10001
EXPOSE 5000
CMD ["python", "app.py"]
