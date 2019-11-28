from flask import Flask
import  json
from service.app_manager import AppManager
from file_handler.handler import FileHandler as ch


OK_STATUS = 200

app = Flask(__name__)
app_manager = AppManager(ch.read_csv())

def create_response(data,response_code=OK_STATUS):
    json_response = json.dumps({ 'response' :data,
                                 'status' : response_code},
                               indent=4)
    return app.response_class(response=json_response,status=response_code,mimetype='application/json')

@app.route('/getApp')
def get_app():
   data = app_manager.assembly_csv_in_a_dict()
   return create_response(data)

if __name__ == '__main__':
   app.run()