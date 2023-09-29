
FROM python:3.9.7

WORKDIR /EXAMPLE

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

EXPOSE 80/tcp
