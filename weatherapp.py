import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QListWidget
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

API_KEY = "8fa3aec35131a801438db41a6c1822b9"

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Forecast App")
        self.setStyleSheet("background-color: white;")
        self.recent_searches = []

        # Screen dimensions
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Overlay size and position
        overlay_width = 800
        overlay_height = 500
        overlay_x = (screen_width - overlay_width) // 2
        overlay_y = (screen_height - overlay_height) // 2

        # Background image
        bg_label = QLabel(self)
        pixmap = QPixmap("/Users/momeenaazhar/Desktop/Weather Forecast App/images for the project/weather_background.jpg")
        if pixmap.isNull():
            print("⚠️ Failed to load background image. Check the file path.")
        bg_label.setPixmap(pixmap)
        bg_label.setScaledContents(True)
        bg_label.setGeometry(0, 0, screen_width, screen_height)

        # Overlay widget
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet("""
            background-color: rgba(255, 255, 255, 180);
            border-radius: 20px;
        """)
        self.overlay.setGeometry(overlay_x, overlay_y, overlay_width, overlay_height)

        # Layouts
        layout = QVBoxLayout()

        # Title
        self.title_label = QLabel("<h1><b>WEATHER FORECAST APP</b></h1>")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Search bar
        input_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setFont(QFont("Arial", 14))
        input_layout.addWidget(self.city_input)

        self.search_button = QPushButton("Search")
        self.search_button.setFont(QFont("Arial", 12))
        self.search_button.clicked.connect(self.get_weather)
        input_layout.addWidget(self.search_button)
        layout.addLayout(input_layout)

        # Weather result
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        self.result_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.result_label)

        # Recent searches
        self.recent_label = QLabel("<b>Recent Searches:</b>")
        self.recent_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.recent_label)

        self.recent_list = QListWidget()
        layout.addWidget(self.recent_list)

        self.overlay.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.result_label.setText("<b>Please enter a city name.</b>")
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather = data["weather"][0]["description"].title()
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]

                result_html = (
                    f"<div align='center'>"
                    f"<p><b>🌍 Weather in {city.title()}:</b></p>"
                    f"<p><b>⛅ Condition: {weather}</b></p>"
                    f"<p><b>🌡️ Temperature: {temp}°C</b></p>"
                    f"<p><b>💧 Humidity: {humidity}%</b></p>"
                    f"<p><b>🌬️ Wind Speed: {wind} m/s</b></p>"
                    f"</div>"
                )
                self.result_label.setText(result_html)

                if city.title() not in self.recent_searches:
                    self.recent_searches.append(city.title())
                    self.recent_list.addItem(city.title())
            else:
                self.result_label.setText("<b>City not found. Please try again.</b>")

        except Exception as e:
            self.result_label.setText("<b>Error retrieving data. Check your connection.</b>")
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.showFullScreen()
    sys.exit(app.exec_())
