from flask import Flask, render_template, request
from flask_cors import CORS
from wp_controller import Weather_Controller

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/weatherinfo', methods=['POST','GET'])
def weatherinfo():
    if request.method == 'POST':
        data = request.json
        input_location = data['location']

        weather_info = Weather_Controller()

        geo_location = weather_info.getLocation(input_location)
        if geo_location == None:
            location_info = "Hey there! You don't seem like an earthling. Is it a hot spot in Mars?"
            report_template = render_template('report_view.html', weather_location=location_info)
            return report_template

        location_info = geo_location.address
        weather_report = weather_info.getWeatherInfo(data, geo_location)

        report_template = render_template('report_view.html', weather_location=location_info, weather_reports=weather_report)

    return report_template

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')