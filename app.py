from flask import Flask, render_template, request
from flask_cors import CORS
from wp_controller import Weather_Controller
import speech_recognition as sr


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
            location_info = "Hey there! You don't seem like an earthling. Is it a hot spot on Mars?"
            return location_info
        elif type(geo_location)==str:
            return geo_location

        location_info = geo_location.address
        weather_report = weather_info.getWeatherInfo(data, geo_location)

        report_template = render_template('report_view.html', weather_location=location_info, weather_reports=weather_report)

    return report_template

@app.route('/speechinput',methods=['POST','GET'])
def speechinput():
    if request.method == 'POST':

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text_input = r.recognize_google(audio)
            print("You said: " + text_input)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text_input


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')