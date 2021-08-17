FROM python:3.8

WORKDIR /usr/src/alternatecms

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["django", "run", "-h", "0.0.0.0"]