FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ARG APP_FILE=catalog.py
COPY catalog.py cart.py ./
ENV APP_FILE=${APP_FILE}
USER 10001
CMD ["sh", "-c", "python $APP_FILE"]
