import requests
import pandas as pd 



coins_list = ["bitcoin", "etherium", "bnb", "tether", "solana", "tron"]


def get_coins_data(a):

    url = "https://api.coingecko.com/api/v3/simple/price"

    try:
        for coin in coins_list:
            params = {

                "ids" : coins_list,  
                'vs_currencies' : 'usd, gbp'

            }
            r = requests.get(url, params=params)
            data = r.json()
            df = pd.DataFrame(data).T
            print(df)
    except requests.exceptions.InvalidJSONError:
        print("not found data")
      
print(get_coins_data(coins_list))