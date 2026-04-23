import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(r.status_code)

# print(r.text) # gives responce as string

# print(api_data)
if(r.status_code == 200):
    api_data = r.json() # converting the response into json 
    with open("D:\DataEngineering\Sync\data.json", "wb") as f:
        f.write(r.content)
    print("Json file saved")
else:
    print("Invalid url")