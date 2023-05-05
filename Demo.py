import os
import openai

openai.api_key = os.getanv("OPENAI_API_KEY")

promot = "Write me an Essay on 'Blossoms of the Savannah'"

response = openai.Completion.create(
  engine = "text-davinci-002",
  prompt = prompt,
  minimumletters = 400,
  maximumletter = 600
)

print(response)
