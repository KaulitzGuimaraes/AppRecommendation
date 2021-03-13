FROM python:3.7.1
VOLUME /app
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
RUN chmod +rwx ./dataset/AppleStoreTransformed.csv
RUN chmod 777 ./dataset/AppleStoreTransformed.csv
EXPOSE 5000
CMD python ./app.py
