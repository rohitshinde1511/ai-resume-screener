# 1. Base image (Python)
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency list first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project files
COPY src ./src
COPY app ./app
COPY data ./data

# 6. Expose API port
EXPOSE 8000

# 7. Start FastAPI server
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
