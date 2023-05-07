print("=========================================")
print("GPT WITH CMD")
print("*para sair use >quit, >exit ou >quit")
print("=========================================")

import openai

# Set up the OpenAI API client
openai.api_key = input("YOUR_API_KEY (ela pode ser obtida no link https://platform.openai.com/account/api-keys): ")


# Set up the model engine and prompt
model_engine = "text-davinci-003"
prompt = ""

import time
while True:
    query = input("você: ")
    if query.lower() in ["sair", "exit", "quit"]:
        break
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + "\n" + query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    print(response)
    # Pausa por 1 segundo entre cada solicitação
    time.sleep(1)
    
print("Programa encerrado.")





