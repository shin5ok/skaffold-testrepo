from flask import Flask, request, jsonify, render_template
import logging
import os
import requests
import json

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

name = "John"
api = "http://my-api/api"
# reserve string 'Ping'
@app.route('/')
def _root():
    logging.info("access to /")
    res = requests.get(api)
    resdata = json.loads(res.content)
    return render_template("index.html", name=resdata['name'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


