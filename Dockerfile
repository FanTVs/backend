FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt main.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENV DATA_FILE=/app/data/data.txt
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
