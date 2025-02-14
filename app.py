from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://api.open-meteo.com/v1/forecast"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                # Use a geocoding API to get latitude and longitude from the city name
                geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
                geocode_response = requests.get(geocode_url)
                if geocode_response.status_code == 200 and geocode_response.json().get("results"):
                    location = geocode_response.json()["results"][0]
                    latitude = location["latitude"]
                    longitude = location["longitude"]

                    # Fetch weather data
                    params = {
                        "latitude": latitude,
                        "longitude": longitude,
                        "current_weather": "true"
                    }
                    response = requests.get(BASE_URL, params=params)
                    if response.status_code == 200:
                        weather_data = response.json()["current_weather"]
                        weather_data["city"] = location["name"]
                    else:
                        error = "Unable to fetch weather data!"
                else:
                    error = "City not found!"
            except Exception as e:
                error = f"An error occurred: {e}"

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
