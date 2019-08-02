from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語文字化け対策

@app.route('/api/<key>', methods=['POST'])
def post_api(key):
    print (request.headers)
    print ("body: %s" % request.get_data())
    json = request.get_json()  
    json["api"] = key
    json["timestamp"] = datetime.now().isoformat()
    return jsonify(json)  


@app.route('/api/<key>', methods=['GET'])
def get_api(key):
    qs = request.query_string
    qsp = qs.decode("utf-8").split('&')
    resp_data = {
        'api' : key,
        'query_string' : qsp,
        'timestamp' : datetime.now().isoformat()
    }
    return jsonify(resp_data)  

if __name__ == '__main__':
    app.run(debug=True)
