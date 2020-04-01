from flask import Flask, jsonify
import json
app = Flask(__name__)


@app.route('/redfish/v1/Systems/1')
def system():
    with open('system.json') as f:
        temp = json.load(f)
    return jsonify(temp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
