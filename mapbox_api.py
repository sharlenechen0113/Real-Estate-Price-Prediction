# Script to save mapbox map to local directory

import requests
import shutil

FILE = 'test/map.png'


def main():
    API_KEY = 'YOUR_API_KEY'
    geocodes = {
        (-122.4241,37.78)
    }
    for codes in geocodes:
        print(codes[0],codes[1])
        i = 1
        r = requests.get("https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
                         "{},{},15,0,0/400x400?access_token={}}".format(codes[0],codes[1],API_KEY),stream=True)
        with open('test/map{}.png'.format(i),'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        i += 1

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
