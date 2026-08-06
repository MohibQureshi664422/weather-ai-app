from groq import Groq
from django.conf import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)



def ask_ai(question, weather):

    prompt = f"""

You are a helpful weather assistant.

Weather Information:

City: {weather['city']}
Temperature: {weather['temperature']} °C
Condition: {weather['description']}
Humidity: {weather['humidity']} %


User Question:

{question}


Give a simple helpful answer.

"""


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "user",
                "content": prompt
            }

        ]

    )


    return response.choices[0].message.content 