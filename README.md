# Weather Web App

This is a simple web app I made that tells you the **current weather** for any city you type in. It’s built with **Python**, **Flask**, and the **Open-Meteo API** for getting weather and location data.  

Basically, you type a city name, the app figures out its location (latitude & longitude), then shows you the temperature and wind speed right now.

---

## How it works
1. **User inputs a city name** in the search box.
2. **Geocoding request** → The app calls the Open-Meteo geocoding API to get latitude and longitude.
3. **Weather request** → The app uses those coordinates to call the Open-Meteo weather API.
4. **Display** → The page shows:
   - City name
   - Temperature in °C
   - Wind speed in km/h
5. If something fails, it shows an error message instead.
