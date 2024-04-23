from flask import Flask, render_template, request
from weather_api import get_weather, get_weather_details
from model import Weather
from datetime import datetime as dt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def show_weather():
    city = request.form['city']
    current_weather = get_weather(city)
    weather_details = get_weather_details(current_weather)

    return render_template('weather.html', city=city, weather_details=weather_details)

if __name__ == '__main__':
    app.run(debug=True)
