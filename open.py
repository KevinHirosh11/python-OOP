import openai

from api_key import api_key

openai.api_key = api_key

completion = openai.ChatCompletion()

def Reply(query):
    prompt = f"Kevin: {query}\n Jarvis"
    response = completion.create(prompt=prompt, engine="text-davinci-002")
    answer = response.choices[0].text.strip()
    return answer

ans = Reply("What is the data science?")
print(ans)
