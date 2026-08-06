from django.shortcuts import render
import requests
from django.conf import settings
from .ai import ask_ai



def home(request):

    weather_data = None
    forecast_data = None
    ai_answer = None
    error = None


    city = request.GET.get("city")
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")



    # AI question
    question = request.GET.get("question")



    # Weather API

    if city:

        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={settings.WEATHER_API_KEY}"
            "&units=metric"
        )


    elif lat and lon:

        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}"
            f"&lon={lon}"
            f"&appid={settings.WEATHER_API_KEY}"
            "&units=metric"
        )


    else:

        return render(request, "weather/home.html")



    response = requests.get(weather_url)

    data = response.json()



    if response.status_code == 200:


        weather_data = {

            "city": data["name"],

            "temperature": data["main"]["temp"],

            "feels_like": data["main"]["feels_like"],

            "humidity": data["main"]["humidity"],

            "wind": data["wind"]["speed"],

            "pressure": data["main"]["pressure"],

            "description": data["weather"][0]["description"],

            "icon": data["weather"][0]["icon"],

        }



        # AI Response

        if question:

            ai_answer = ask_ai(
                question,
                weather_data
            )



    else:

        error = data.get("message")




    return render(
        request,
        "weather/home.html",
        {
            "weather": weather_data,

            "forecast": forecast_data,

            "ai_answer": ai_answer,

            "error": error
        }
    )