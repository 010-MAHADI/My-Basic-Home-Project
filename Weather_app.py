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



বাংলায় বর্ণনা

কোডটি একটি সাধারণ Weather App যা OpenWeatherMap API ব্যবহার করে কোন একটি শহরের বর্তমান আবহাওয়ার তথ্য নিয়ে আসে। নিচে লাইন বাই লাইন ব্যাখ্যা করছি:


---

🔹 import requests

👉 requests একটি Python লাইব্রেরি যা HTTP রিকোয়েস্ট পাঠাতে ব্যবহার করা হয় (যেমন: GET, POST)।
এই প্রজেক্টে আমরা OpenWeatherMap API তে GET রিকোয়েস্ট পাঠাবো।


---

🔹 def fetch_weather_data(location):

👉 এটি একটি ফাংশন যার কাজ হলো ইউজার দ্বারা দেওয়া লোকেশনের আবহাওয়া তথ্য API থেকে সংগ্রহ করা।


---

🔹 api_key='9663bf9d35800c25286db2de1dad0d36'

👉 এটি তোমার OpenWeatherMap API Key। এই key দিয়ে প্রমাণ করা হয় যে তুমি API ব্যবহার করার অনুমতি পেয়েছো।


---

🔹 base_url="https://api.openweathermap.org/data/2.5/weather"

👉 এটি হলো সেই API এর মূল URL যা থেকে আবহাওয়ার ডেটা আসবে।


---

🔹 params={"q":location,"appid":api_key}

👉 এটি হলো URL এর কুয়েরি প্যারামিটার।

q এর মান হচ্ছে লোকেশন (শহরের নাম)

appid হচ্ছে API key



---

🔹 response=requests.get(base_url,params=params)

👉 GET রিকোয়েস্ট পাঠানো হচ্ছে OpenWeatherMap API তে।


---

🔹 if response.status_code==200:

👉 চেক করা হচ্ছে HTTP রেসপন্স কোড 200 কিনা। 200 মানে: সফলভাবে ডেটা পাওয়া গেছে।


---

🔹 weather_data=response.json()

👉 যদি সফল হয়, তাহলে JSON ফরম্যাটে ডেটা কনভার্ট করে weather_data নামক ভেরিয়েবলে সংরক্ষণ করা হচ্ছে।


---

🔹 return weather_data

👉 ফাংশনের বাইরে সেই ডেটা রিটার্ন করছে।


---

🔹 else: (যদি স্ট্যাটাস কোড 200 না হয়)

👉 তাহলে এরর মেসেজ প্রিন্ট করবে এবং None রিটার্ন করবে।


---

🔹 except requests.RequestException as e:

👉 যদি ইন্টারনেট সমস্যা বা অন্য কোনো এক্সসেপশন হয়, তাহলে সেটাও হ্যান্ডেল করা হচ্ছে।


---

🔹 def print_weather_data(weather_data):

👉 এই ফাংশনের কাজ হলো প্রাপ্ত আবহাওয়া ডেটা সুন্দরভাবে প্রিন্ট করে দেখানো।


---

🔹 if weather_data:

👉 চেক করছে আসলেই ডেটা এসেছে কিনা।


---

🔹 নিচের লাইনে প্রিন্ট করা হচ্ছে:

Location: → শহরের নাম

Description: → আবহাওয়ার বর্ণনা (যেমন "clear sky")

Temperature: → ডিগ্রি কেলভিন থেকে সেলসিয়াসে কনভার্ট করে দেখানো হচ্ছে temp - 273.15

Humidity: → বাতাসে আর্দ্রতার পরিমাণ

Wind Speed: → বাতাসের গতি (m/s)



---

🔹 def main():

👉 প্রোগ্রামের মূল ফাংশন


---

🔹 location=input("Enter Location Name:")

👉 ইউজার থেকে শহরের নাম ইনপুট নিচ্ছে


---

🔹 weather_data= fetch_weather_data(location)

👉 fetch_weather_data() ফাংশন কল করে API থেকে ডেটা আনছে


---

🔹 print_weather_data(weather_data)

👉 আবহাওয়ার ডেটা প্রিন্ট করছে


---

🔹 main()

👉 প্রোগ্রাম চালু করার জন্য main() ফাংশন কল করা হচ্ছে।


---