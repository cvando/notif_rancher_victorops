FROM python:3.7-alpine
ADD notifier /notifier
RUN pip install requests \
                python-dotenv \
                klein
EXPOSE 8090/tcp

CMD [ "python", "./notifier/main.py" ]