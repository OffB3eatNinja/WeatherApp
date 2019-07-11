from flask import Flask, render_template, request
from flask_cors import CORS
from wp_controller import Weather_Controller

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')