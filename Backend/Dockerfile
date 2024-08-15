FROM python:3-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 5432
CMD python3 -m uvicorn main:app --host 0.0.0.0 --reload

