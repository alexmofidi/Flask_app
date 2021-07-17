FROM alpine:3.7

EXPOSE 3031

VOLUME /usr/src/app

WORKDIR /usr/src/app

ENV FLASK_APP=test

RUN apk add --no-cache \
        uwsgi-python3 \
        python3 \
        bash \
        py-pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "main:app" ]
