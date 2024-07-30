from tkinter import *#
import requests#get user requests
from datetime import datetime    
import json #interface with user and acess essential information
from PIL import Image, ImageTk  #import image from folder

root = Tk()
root.geometry("400x500")
root.resizable(10, 10)
root.title("Weather APP-AskPython.com")

city_value = StringVar()

def show_weather():
    api_key = "01adbb73ffbfbeafdf5d7e4798e53800"#api key from open weather app
    city_name = city_value.get()
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    response = requests.get(weather_url)
    weather_info = response.json()
    #used to acess data fro weather api
    if weather_info['cod'] == 200:#cod=codification and 200 indicates sucessful responce
        kelvin = 273
    
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        
        sunrise_time = datetime.utcfromtimestamp(sunrise + timezone).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(sunset + timezone).strftime('%Y-%m-%d %H:%M:%S')
        
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    tfield.delete(1.0, END)
    tfield.insert(INSERT, weather)

Label(root, text='Enter City Name', font='Times 14 bold').pack(pady=10)  
inp_city = Entry(root, textvariable=city_value, width=24, font='Times 14 bold')  
inp_city.pack()

Button(root, command=show_weather, text="Check Weather", font="Times 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

Label(root, text="The Weather is:", font='Times 12 bold').pack(pady=10) 

tfield = Text(root, width=46, height=10, font='Times 10')  
tfield.pack()

# Load an image
img = Image.open("C:\\Users\\mural\\OneDrive\\Pictures\\rainmeter logo png\\MURALI NEW LOGO.png")  # Replace with your image path
img = img.resize((200, 100))  # Resize the image as needed

photo = ImageTk.PhotoImage(img)
img_label = Label(root, image=photo)
img_label.pack(pady=10)

root.mainloop()