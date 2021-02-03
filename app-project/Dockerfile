FROM openshift/python:latest
VOLUME app
RUN cat requirements.txt
COPY . /app
WORKDIR app
RUN pwd
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod -R 777 ./
CMD python ./app.py
