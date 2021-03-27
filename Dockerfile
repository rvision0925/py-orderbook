FROM eu.gcr.io/our-proj/base/python:3.7.5-slim-buster
ENV TZ=Etc/UTC
WORKDIR /srv/app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "/srv/app/main.py"]
