from flask import Flask, request, jsonify, render_template
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

name = "John"
# reserve string 'Ping'
@app.route('/')
def _root():
    logging.info("access to /")
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


