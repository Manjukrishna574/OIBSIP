import tkinter as tk
import requests

API_KEY = "62a33eeca6650e78ba76d315dc3eca36"

def get_weather():

    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        result_label.config(text=" City not found", fg="red")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    condition = data["weather"][0]["description"]

    result = f"""
 City : {city}

 Temperature : {temp} °C
 Humidity : {humidity} %

 Wind Speed : {wind} m/s

 Condition : {condition}
"""

    result_label.config(text=result, fg="white")


# Window
root = tk.Tk()
root.title("Weather App")

# Window size
width = 500
height = 500

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Center position
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

root.configure(bg="#0f172a")


# Card frame
frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=30,
    pady=30
)

frame.place(relx=0.5, rely=0.5, anchor="center")


# Title
title = tk.Label(
    frame,
    text="Weather App",
    font=("Segoe UI",24,"bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

title.pack(pady=10)


# Entry
city_entry = tk.Entry(
    frame,
    font=("Segoe UI",14),
    width=22,
    justify="center",
    bd=2
)

city_entry.pack(pady=15)

city_entry.insert(0,"Enter City")


# Button
search_btn = tk.Button(
    frame,
    text="Get Weather",
    font=("Segoe UI",12,"bold"),
    bg="#38bdf8",
    fg="black",
    width=15,
    pady=5,
    command=get_weather
)

search_btn.pack(pady=15)


# Result
result_label = tk.Label(
    frame,
    font=("Segoe UI",12),
    bg="#1e293b",
    fg="white",
    justify="left"
)

result_label.pack(pady=20)


root.mainloop()