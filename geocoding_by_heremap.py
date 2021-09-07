
import json
import requests


API_KEY = "YOUR_API_KEY"
def main():
    places = '台北市內湖區內湖路一段735號'
    url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey={}&searchtext={}".format(API_KEY,places)
    response = requests.request("GET", url)
    data = json.loads(response.text)
    lat = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    lng = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    print((lat,lng))

if __name__ == '__main__':
    main()