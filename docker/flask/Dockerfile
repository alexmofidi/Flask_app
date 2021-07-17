FROM alpine:3.7

EXPOSE 80

VOLUME /usr/src/app

WORKDIR /usr/src/app

ENV FLASK_APP=main
ENV FLASK_DEBUG=true
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/nlp-319817-de3414e98d40.json"

RUN apk add \
        uwsgi-python3 \
        python3 \
        python3-dev \
        bash \
        g++ \
        g++ \
        gcc \
        musl-dev \
        py-pip \
        pkgconfig \
        git \
        openldap \
        libcurl \
        libc-dev

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip install --upgrade google-cloud-language

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "80"]