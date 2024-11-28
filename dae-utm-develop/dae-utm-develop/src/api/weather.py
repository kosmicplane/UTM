from src.constants.lib import *
def meteorological_values(latitude, longitude):
    ##!! Satellite coordinates for start and end are in this section !!
    lat = latitude ## START LATITUDE, SET TO ENVIGADO
    lon = longitude ## START LONGITUDE, CURRENTLY FIXED
    ## The storage lists for data are in this section
    '''Empty for now'''
    ### THE MAIN INFORMATION LOOP, WHERE LATITUDE IS ITERATED
    res1 = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=7c756e9dba0d0627e519bac718f21da4'.format(lat,lon))#### KEY PART, HERE THE API SERVER IS CALLED TO QUERY THE INFORMATION
    if res1:
        dic = res1.json()## THE DATA IS TRANSLATED INTO A DICTIONARY
        name_dic = dic['name']### EXTRACTING THE POINT NAME
        temp_dic = dic['main']['temp']-273.15## EXTRACTING TEMPERATURE
        main_dic = dic['weather'][0]['main']### WEATHER TYPE
        desc_dic = dic['weather'][0]['description']#### WEATHER INFORMATION
        humidity_dic = dic['main']['humidity']# AIR HUMIDITY
        pressure_dic = dic['main']['pressure']# PRESSURE
        vis_dic = dic['visibility']## VISIBILITY IN METERS
        vel_dic = dic['wind']['speed']## WIND SPEED
        ### THE DATA IS THEN PLACED INTO LISTS OF THEIR RESPECTIVE CATEGORIES
        sms = ("The atmospheric variables for the {} sector are as follows: \n Summary: {}  Description: {} with temperature: {}°C, pressure: {}Hpa, wind speed: {}m/s, humidity: {}%, visibility: {}m".format(name_dic,main_dic,desc_dic,temp_dic,pressure_dic,vel_dic,humidity_dic,vis_dic))
    else:
        print('Response Failed')
        try: meteorological_values(lat,lon) # IF THE OPERATION FAILS, IT WILL TRY AGAIN
        except ValueError:
            print("THE SYSTEM HAS STOPPED WORKING, WE'RE SORRY")
    meteo_list = [name_dic,main_dic,desc_dic,temp_dic,pressure_dic,vel_dic,humidity_dic,vis_dic]
    print(dic)
    return meteo_list###RETURNS THE VARIABLES EXTRACTED FROM THE QUERY
#print(meteorological_values(6.78,-755))ACTIVATE THIS IF U WANT TO TEXT DE API
