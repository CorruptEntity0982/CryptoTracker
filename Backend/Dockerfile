FROM python:3-alpine
WORKDIR /app
ENV EMAIL_PASS=lqnudmognpkgojei
ENV EMAIL_USER=shashank02.dubey@gmail.com
#ENV SQL_ALCHEMY_DATABASE_URL=postgresql://postgres:try12345@localhost:5432/CryptoTracker
ENV SQL_ALCHEMY_DATABASE_URL=postgresql://postgres:try12345@host.docker.internal:5432/CryptoTracker
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 5432
CMD python3 -m uvicorn main:app --host 0.0.0.0 --reload

