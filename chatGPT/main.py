import openai

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "What is the difference between celsius and fahrenheit ?"
        }
    ]
)

print(response)
# I am a comment

