# yahoo_api.py
import requests
import pprint
url = r'''https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22St.%20Petersburg%22)%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'''
data = requests.get(url).json()
forecast = data['query']['results']['channel']['item']['forecast']
result = []
for day in forecast:
    result.append({'date': day['date'], 'high_temp': day['high']})
pprint.pprint(result)
