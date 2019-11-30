FROM python:3.6-alpine
ADD notifier /notifier
RUN pip install requests 
EXPOSE 8080/tcp

CMD [ "python", "./notifier/main.py" ]