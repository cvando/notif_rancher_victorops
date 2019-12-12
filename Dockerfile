FROM python:3.7-alpine
ADD notifier /notifier
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install klein requests \
                python-dotenv \
                klein
RUN apk del .build-deps gcc musl-dev
EXPOSE 8090/tcp

CMD [ "python", "./notifier/main.py" ]