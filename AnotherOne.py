#This one was suggested to me by my Friend Bethuel (https://github.com/bethropolis)
#Check it out

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_essay(prompt): # I made a function, you can call this from anywhere
    response = openai.Completion.create(
        engine="text-davinci-002", #gpt-3.5 turbo is also good
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024, # for an essay this is good
        n=1, # number of response
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

# Example usage 
prompt = input("what is your essay query: ")
response = generate_essay(prompt)
print(response)


# Be free to make Changes
