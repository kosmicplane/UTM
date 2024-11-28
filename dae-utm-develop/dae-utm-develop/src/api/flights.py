import requests

'''
lat_min = 5.319854  # Approximate minimum latitude
lat_max = 8.918149  # Approximate maximum latitude
lon_min = -77.654173  # Approximate minimum longitude
lon_max = -75.162506  # Approximate maximum longitude
'''

### THIS IS ACTIVATED IF YOU WANT TO KNOW ABOUT AIRCRAFT IN COLOMBIA
lat_min = -4.231687
lat_max = 12.514047
lon_min = -82.937515
lon_max = -66.857530

def radar_flights():
    # Make a request to the OpenSky API
    url = f"https://opensky-network.org/api/states/all?lamin={lat_min}&lamax={lat_max}&lomin={lon_min}&lomax={lon_max}"
    response = requests.get(url, auth=('jebaeros', '192837465'))
    
    # Check the response status code
    if response.status_code == 200:
        # Get aircraft data
        data = response.json()
        data = data['states']
        data = list(data)
    else:
        # Handle the case of an error in the response
        print('Error obtaining aircraft information:', response.text)
    return data

#print(radar_flights()) ACTIVATE THIS IF U WANT TO CHECK THE API IS WORKING