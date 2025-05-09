# 🌦️ **Weather Forecast App**

This is a **Weather Forecast App** built using **PyQt5** and the **OpenWeatherMap API** to provide current weather information and a 7-day forecast for any city entered by the user.

---

## 🚀 Features

- 🔍 Search weather information by city name.
- 📊 Displays current weather details including:
  - 🌡️ Temperature (in Celsius)
  - ☁️ Weather condition (e.g., sunny, cloudy)
  - 💧 Humidity
  - 🌬️ Wind speed
- 🕒 Keeps a history of recent city searches.
- 🎨 Beautiful GUI with a background image and transparent overlay.

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **PyQt5**
- **Requests**

### 📦 Install Required Packages

```bash
pip install PyQt5 requests

## ⚙️ Setup Instructions

1. 🔑 Obtain an API Key from OpenWeatherMap:
	•	Sign up at OpenWeatherMap.
	•	After registration, go to your account and copy your API Key.

2. 🧩 API Key Setup:

Replace the API_KEY placeholder in the code with your actual OpenWeatherMap API key:
API_KEY = "your_openweathermap_api_key"

3. ▶️ Run the App:

Use the following command in your terminal to run the app:
python weather_app.py

## 🧠 **How the App Works** 

1. 🖥️ User Interface
	•	The app starts with a graphical interface.
	•	Enter a city name in the input box and click Search.
	•	Weather details for that city are fetched and shown including:
	•	⛅ Weather condition
	•	🌡️ Temperature
	•	💧 Humidity
	•	🌬️ Wind speed

2. 📋 Recent Searches
	•	The app keeps a list of previously searched cities.
	•	Clicking on any of them fetches the weather again.

3. 🖼️ Background Image
	•	A customizable background image enhances the visual appearance of the app.

4. 🚨 Error Handling
	•	If a city is not found:
❌ “City not found. Please try again.”
	•	If there’s a connection issue:
❌ “Error retrieving data. Check your connection.”

##📸 Screenshots
/Users/momeenaazhar/Desktop/Weather Forecast App/screenshots/Screenshot1.png
/Users/momeenaazhar/Desktop/Weather Forecast App/screenshots/Screenshot2.png

##📝 Notes
	•	The app fetches real-time weather for a single city at a time.
	•	An active internet connection is required to fetch data from OpenWeatherMap.
	•	You can customize the background image by changing the image path in the code.

##🤝 Contributing

Feel free to fork the repository, create a branch, make improvements, and submit a pull request!

## Made by
**Momeena Azhar**
