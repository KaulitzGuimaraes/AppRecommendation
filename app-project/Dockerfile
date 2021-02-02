FROM python:3.7.1
COPY . /
RUN pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN pip install -r requirements.txt
EXPOSE 5000
RUN chmod -R 777 *.py *.csv
CMD python ./app.py
