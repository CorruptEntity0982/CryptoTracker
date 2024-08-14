FROM python:3-alpine
WORKDIR /Backend
ENV EMAIL_PASS="lqnu dmog npkg oje"
ENV EMAIL_USER="shashank02.dubey@gmail.com"
ENV SQL_ALCHEMY_DATABASE_URL='postgresql://postgres:try12345@localhost/CryptoTracker'
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 5432
CMD ["cd","Backend","python3", "-m", "uvicorn", "main:app", "--reload"]
