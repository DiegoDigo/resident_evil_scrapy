FROM python:3.9-alpine

WORKDIR /app

ARG USERNAME
ARG PASSWORD
ARG PORT=8000

ADD requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c" ,"uvicorn main:app --proxy-headers --host 0.0.0.0 --port ${PORT} --timeout-keep-alive 60"]
