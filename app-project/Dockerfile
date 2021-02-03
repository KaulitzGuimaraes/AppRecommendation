FROM openshift/python:latest
RUN chmod -R 777 ./
VOLUME app
RUN cat requirements.txt
COPY . /app
WORKDIR app
RUN pwd
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000

CMD python ./app.py
