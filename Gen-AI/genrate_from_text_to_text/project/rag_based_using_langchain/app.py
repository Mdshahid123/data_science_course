# making api call to the openai server using langchain library

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 

# Load the environment variables from the .env file into the system environment
load_dotenv() 


# Initialize Ollama using the unified function
model = init_chat_model(
    model="ollama:llama3.1", 
    temperature=0
)


# You can now invoke it exactly like any other chat model
response = model.invoke("Why is the sky blue?")
print(response.content)
 




