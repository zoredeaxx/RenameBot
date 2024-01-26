FROM python:3.10
WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install -r requirements.txt
#ENV PORT = 8080
EXPOSE 5000
CMD ["python", "bot.py"]
