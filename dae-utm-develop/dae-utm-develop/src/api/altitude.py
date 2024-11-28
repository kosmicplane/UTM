import requests

def get_altitude(lat, lng): # Altitude points function
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}" # API call key
    response = requests.get(url) # Obtained response
    data = response.json() # Converted to JSON format
    
    if 'results' in data: # Discarding empty data
        altitude = data['results'][0]['elevation']
        return altitude
    else:
        return None
#print(get_altitude(6.78,-75))#ACTIVATE THIS IF U WANT TO CHECK IF THE API IS WORKING