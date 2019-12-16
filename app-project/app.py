import random

from flask import Flask
from flask_cors import CORS
import  json
from service.app_manager import AppManager
from file_handler.handler import FileHandler as ch


OK_STATUS = 200
INTERNAL_SERVICE_ERROR = 500
DATA_ERROR =[]


app = Flask(__name__)
app_manager = AppManager(ch.read_csv())
CORS(app)

def create_response(data,response_code=OK_STATUS):
    json_response = json.dumps({ 'response' :data,
                                 'status' : response_code},
                               indent=4)
    return app.response_class(response=json_response,status=response_code,mimetype='application/json')

@app.route('/getApp')
def get_app():
    try:
       data = app_manager.assembly_csv_in_a_dict()
       random_number = random.randint(0, len(data))
       return create_response(data[random_number])
    except Exception as e :
        return create_response([str(e),INTERNAL_SERVICE_ERROR])

@app.route('/getAppCluster')
def get_app_cluster():
    try:
       data = app_manager.assembly_csv_in_a_dict()
       return create_response(data[:10])
    except Exception as e :
        return create_response([str(e),INTERNAL_SERVICE_ERROR])

if __name__ == '__main__':
   app.run(port="5000",host="localhost")