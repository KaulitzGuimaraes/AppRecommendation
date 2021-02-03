FROM python:3.7.1
VOLUME app
RUN ls -l
COPY . /app
RUN ls -l
WORKDIR app
RUN pwd
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod -R 777 ./
CMD python ./app.py
