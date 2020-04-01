from flask import Flask, jsonify
import json
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'hello'
app.config['BASIC_AUTH_PASSWORD'] = '123'

basic_auth = BasicAuth(app)

@app.route('/redfish/v1/Systems/1')
@basic_auth.required
def system():
    with open('system.json') as f:
        temp = json.load(f)
    return jsonify(temp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
