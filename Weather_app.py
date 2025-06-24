import requests
def get_weather_data(location):
    #get an api from openweathermap.org
    api_key='9663bf9d35800c25286db2de1dad0d36'
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params={"q":location,"appid":api_key}
    try:
        response=requests.get(base_url,params=params)
        if response.status_code==200:
            weather_data=response.json()
            return weather_data
        else:
            print("Faild to Fetch Weather Data.Status Code:",response.status_code)
            return None
    except requests.RequestException as e:
        print("Eroor Occurred during request:",e)
        return None
def print_weather_data(weather_data):
    if weather_data:
        print("Basic Weather Data")
        print("Location:",weather_data['name'])
        print("Description:",weather_data['weather'][0]['description'])
        print("Temperature(Celsius):",weather_data['main']['temp']-273.15)
        print("Humidity:",weather_data['main']['humidity'])
        print("Wind Speed (m/s):",weather_data['wind']['speed'])
    else:
        print("No weather data available.")
def main():
    location=input("Enter Location Name:")
    weather_data= get_weather_data(location)
    print_weather_data(weather_data)
main()