# WeatherApp

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Functionality](#functionality)
## Introduction

WeatherApp is a Python-based application that provides real-time weather information for any city. The application uses the OpenWeatherMap API to fetch weather data and displays it in a user-friendly graphical interface created with Tkinter.

<img width="389" alt="image" src="https://github.com/user-attachments/assets/88b74861-5cd6-4f8c-b99a-17649f17edb5">


## Features

- **Real-Time Weather Data**: Fetches and displays current weather information for any city.
- **Graphical User Interface**: User-friendly interface built with Tkinter.
- **Weather Details**: Displays temperature, feels like temperature, pressure, humidity, wind speed, cloudiness, and description.
- **Sunrise and Sunset Times**: Shows the local time for sunrise and sunset.
- **Error Handling**: Provides user feedback if the city is not found.

## Functionality

### Fetch Weather Data
- **Library**: `requests`
- **Function**: `show_weather()`
- **Description**: Sends a request to the OpenWeatherMap API and processes the response to display weather information.

### Display Weather Information
- **Library**: `tkinter`
- **Widgets**: `Label`, `Entry`, `Button`, `Text`
- **Description**: Uses various Tkinter widgets to create the graphical interface and display weather information.

### Image Display
- **Library**: `PIL`
- **Function**: `Image.open()`, `ImageTk.PhotoImage()`
- **Description**: Loads and displays an image in the application.

## Technologies Used

- **Python**: The primary programming language used.
- **Libraries**: `requests`, `tkinter`, `PIL` (Pillow)
- **API**: [OpenWeatherMap API](https://openweathermap.org/api)


