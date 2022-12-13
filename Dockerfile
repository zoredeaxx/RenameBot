FROM python:3.10
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
#ENV PORT = 8080
EXPOSE 5000
CMD ["python", "bot.py"]
