import random

from flask import Flask
from flask_cors import CORS
import json
from service.app_manager import AppManager
from file_handler.handler import FileHandler as ch
from machine_learning.model import  KmeansModel
from flask import request
OK_STATUS = 200
INTERNAL_SERVICE_ERROR = 500
DATA_ERROR = []

app = Flask(__name__)
app_manager = AppManager(ch.read_csv())
svc = ch.read_csv("./dataset/AppleStoreTransformed.csv")
svc_2 = ch.read_csv("./dataset/AppleStoreTransformed.csv")
km = KmeansModel(csv_raw=svc_2, csv_t=svc,n_clusters=20)
CORS(app)


def create_response(data, response_code=OK_STATUS):
    json_response = json.dumps({'response': data,
                                'totalElements' : len(data),
                                'status': response_code},
                               indent=4)
    return app.response_class(response=json_response, status=response_code, mimetype='application/json')


@app.route('/getApp')
def get_app():
    try:
        data = app_manager.assembly_csv_in_a_dict()
        random_number = random.randint(0, len(data))
        return create_response(data[random_number])
    except Exception as e:
        return create_response([str(e), INTERNAL_SERVICE_ERROR])


@app.route('/getAppCluster')
def get_app_cluster():
    try:
        row = request.args.get('index')
        cluster = km.get_cluster(index=row)
        data = app_manager.assembly_csv_in_a_dict(index_array=cluster)
        return create_response(random.sample(data, 10))
    except Exception as e:
        return create_response([str(e)],response_code=500)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0")
