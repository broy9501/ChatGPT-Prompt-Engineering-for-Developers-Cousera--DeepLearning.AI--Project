from openai import OpenAI
import panel as pn

OPENAI_KEY = "API_KEY"  # Replace with your actual OpenAI API key
key = OpenAI(api_key=OPENAI_KEY)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = key.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = key.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    # print(str(response.choices[0].message))
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


""""
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]


response = get_completion_from_messages(messages, temperature=1)
print(response)  # Output: "The 2020 World Series was played at Globe Life Field in Arlington, Texas."


messages = [
    {"role": "system", "content": "You are friendly chatbot."},
    {'role': 'user', 'content': 'Hi, my name is Bishal.'}
]

response = get_completion_from_messages(messages, temperature=1)
print(response)  # Output: "Hello Bishal! It's nice to meet you. How can I assist you today?"
"""
