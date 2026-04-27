import requests
import pandas as pd

api_key = 'bc6dbd7a60a0915ffb4c055fc35dfecc'
 
user_input = input('Enter city: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# print(weather_data.status_code) # checking the status
weather = weather_data
print(weather_data.json())
df = pd.DataFrame(weather)
print(df)
# print(df.shape)
