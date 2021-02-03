FROM openshift/python:latest
RUN chmod -R 777 ./
VOLUME app
COPY . /app
RUN ls
WORKDIR app
RUN pwd
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000

CMD python ./app.py
