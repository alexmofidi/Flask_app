FROM python:3.7.11-buster

EXPOSE 3031

VOLUME /usr/src/app

WORKDIR /usr/src/app

ENV FLASK_APP=main
ENV FLASK_DEBUG=true
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/nlp-319817-de3414e98d40.json"

COPY . .

RUN pip3 install uwsgi  
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
               "--protocol", "uwsgi", \
               "--wsgi", "main:app" ]
