from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語文字化け対策

@app.route('/api/<key>', methods=['POST'])
def post_api(key):
    print (request.headers)
    print ("body: %s" % request.get_data())
    json = request.get_json()
    json["podname"] = os.getenv('K8S_POD_NAME','null')
    json["pod_ip"] = os.getenv('K8S_POD_IP','null')
    json["api"] = key
    json["timestamp"] = datetime.now().isoformat()
    return jsonify(json)


@app.route('/api/<key>', methods=['GET'])
def get_api(key):
    qs = request.query_string
    qsp = qs.decode("utf-8").split('&')
    resp_data = {
        'query_string' : qsp,
        'podname' : os.getenv('K8S_POD_NAME','null'),
        'pod_ip' : os.getenv('K8S_POD_IP','null'),
        'api' : key,
        'timestamp' : datetime.now().isoformat()
    }
    return jsonify(resp_data)

if __name__ == '__main__':
    app.run(debug=True)
