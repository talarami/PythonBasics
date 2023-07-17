
import requests

coinsList = None
currency = "pln"


coinsList = None # przechowanie dostępu do danych zwróconych z serwera za pomocą utworzenia globalnej zmiennej

def getCoinsList():
    global coinsList
    # [ {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}} ... ]
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("response ok")
        data = response.json() # serwer zwraca zwyłky łańcuch znaków string i za pomocą json należy sparsować do jakiejś struktury, do jakichś danych np lista, słownik itd
        print(data[0])
        print("Ilość kryptowalut:" + str(len(data))) # 9990
        coinsList = data

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip # kasowanie białych znaków w łańcuchu znaków i tylko małe litery
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None

getCoinsList()

btcData =  findCoinBySymbol("btc")
print(btcData)

# pobranie danych z rynku odnośnie konkretnej waluty:

def getCoinLastMarketData(coinId):
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin"+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data
    else:
        return None
    
marketData = getCoinLastMarketData(btcData)
print("marketData:", marketData)