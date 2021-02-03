FROM alpine:3.5
RUN apk update
RUN apk add git
RUN apk add --no-cache python3 py3-pip
VOLUME app
WORKDIR app
RUN  ls -la
RUN git clone https://github.com/KaulitzGuimaraes/AppRecommendation.git
WORKDIR app-project
RUN pwd
RUN python3 -m pip install --upgrade pip
ENV HOST="0.0.0.0"
RUN python3 -m pip install -r requirements.txt
RUN chmod -R 777 ./
EXPOSE 5000
CMD python ./app.py
