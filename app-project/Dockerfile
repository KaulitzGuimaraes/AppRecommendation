FROM python:3.7.1
COPY . /
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod -R 777 /app-project
RUN cd /app-project
CMD python ./app.py
