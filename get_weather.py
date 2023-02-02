from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = "your_api_key"
    #url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    url = f"http://api.weatherapi.com/v1/current.json?key=b28f39ca5d844582871174030230202&q={city}&aqi=no"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data


if __name__ == '__main__':
    app.run()
