# This script is used to populate nearby features of a certain latitude/longitude

import requests
import json

def get_nearby(codes,API_KEY):
    R = 500
    lng = codes[1]
    lat = codes[0]
    radius = R
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&keyword=cruise&key={}".format(
        lat, lng, radius, API_KEY)
    payload = {}
    response = requests.request("GET", url, data=payload)
    data = json.loads(response.text)
    return data

def dfs(tree, item,nearby_types):
    for key, value in tree.items():
        ### loop through the result string and add counts to the feature dictionary
        if key == item:
            for features in tree[key]:
                nearby_types[features] = nearby_types.get(features,0)
                nearby_types[features] += 1
        elif isinstance(value, dict):
            nearby_types.update(dfs(value, item,nearby_types))
    return nearby_types

def main():
    API_KEY = 'YOUR_API_KEY'
    # load geocodes in tuples
    geocodes = {
        (-33.8587323, 151.2100055): {}
    }
    for codes in geocodes:
        data = get_nearby(codes,API_KEY)
        nearby_types = {}
        for i in range(len(data['results'])):
            nearby_types = dfs(data['results'][i],'types',nearby_types)
        geocodes[codes] = nearby_types
        print(geocodes)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/