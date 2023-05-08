'''wheather forecact app'''

import argparse
import requests


API_KEY = '901f8348bf708d7e4df25ce9f2770dd9'
API_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def handle_args():
    '''handle arguments'''
    parser = argparse.ArgumentParser(description='forecast weather parser')
    parser.add_argument(
        'city',
        help='name of city for forecast'
    )
    parser.add_argument(
        '-u', '--units',
        help='ttpe of units',
        choices=['metric','imperial','standard'],
        default='standard'

    )
    return parser.parse_args()


def display_wheather(res):
    '''display responce to user'''
    data = res.json()
    city = data['city']['name']
    country = data['city']['country']
    print(f"Forecast if for {city} in {country}: \n")

    forecast_list = data['list'] 

    for item in forecast_list:
        print(item['dt_txt'])
        temp = item['main']['temp']
        # temp = temp_K - 273.15;

        feels_like=item['main']['feels_like']
        whether = item['weather'][0]['main']
        whether_desc = item['weather'][0]['description']

        print(f' - Temp: {temp}')
        print(f' - Feels like: {feels_like}')
        print(f' - Wheather: {whether} - {whether_desc}')
        
    
def main():
    '''entrypoint of scrypt'''
    args = handle_args()
    req_params = {'q': args.city, 'units': args.units, 'appid': API_KEY}
    res = requests.get(API_BASE_URL, params=req_params)
    # print(res.text)
    # print(res.json)

    display_wheather(res)

if __name__ == '__main__':
    main()
