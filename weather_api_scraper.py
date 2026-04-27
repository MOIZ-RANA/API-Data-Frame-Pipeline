import requests 
import pandas as pd 

api_key  = "bc6dbd7a60a0915ffb4c055fc35dfecc"

a  = input("Enter city: ")
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={a}&appid={api_key}&units=metric")

if r.status_code == 200:
    api_data = r.json()
    
    df = pd.json_normalize(api_data)
    print(df[["name", "main.temp", "main.humidity"]])
else:
    print("city not found")

# print(df.shape)
# print(df.columns)