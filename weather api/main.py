import datetime as dt 
import requests 

api_key = 'api_key' #input your own api key

def far_to_cel(fahrenheit): #transformation fahrenheit to celcius
    celcius = (fahrenheit - 32) / 1.8
    return celcius


try: 
    while True :

        city = input("Enter City: ")

        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")


        if data.json()['cod'] == '404': #control if the input exists
            print("No City Found")
            print(f"______________________________________________")

        else:
            response = data.json()

            temp_f = response['main']['temp']
            temp_c = far_to_cel(temp_f)

            feels_like_f = response['main']['feels_like']
            feels_like_c = far_to_cel(feels_like_f)

            wind_speed = response['wind']['speed']

            humidity = response['main']['humidity']
            description = response['weather'][0]['description']

            sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
            sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


            print(f"______________________________________________")

            print(f"Temperature in {city}: {temp_c:.2f}°C or {temp_f:.2f}°F")
            print(f"Temperature in {city} feels like: {feels_like_c:.2f}°C or {feels_like_f:.2f}°F")
            print(f"Humidity in {city}: {humidity}%")
            print(f"Wind speed in {city}: {wind_speed} m/s")
            print(f"General Weather in {city}: {description}")
            print(f"Sunrise in {city}: {sunrise_time} local time.")
            print(f"Sunset in {city}: {sunset_time} local time.")

            print(f"______________________________________________")
            print(f"Press 'Ctrl-C' to end the loop")
            print(f"______________________________________________")


except KeyboardInterrupt :
    print(f"Loop interrupted")
