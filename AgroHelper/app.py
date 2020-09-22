from flask import Flask , render_template, request
import requests

app = Flask(__name__)


country = 'Cameroon'
agro = 'http://api.openweathermap.org/data/2.5/weather?appid=b22003b3d6bd2c2d671782246886dfc3&q='
url = agro + country
json_data = requests.get(url).json()

coord_lon = json_data['coord']['lon']
coord_lat = json_data['coord']['lat']
weather = json_data['weather'][0]['main']
temp = json_data['main']['temp']
f_temp = (temp - 32) * 5/9
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind_speed = json_data['wind']['speed']

clouds = json_data['clouds']['all']
count = country

@app.route('/')

def index():
    
 return render_template('index.html', lon=coord_lon, lat=coord_lat, clouds=clouds, country=count, pressure=pressure,humidity=humidity,  temperature=f_temp,    windspeed=wind_speed)

if __name__ == "__main__":
 app.run(debug=False)
