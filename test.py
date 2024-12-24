import os
from openai import OpenAI

# Configuração da chave de API
api_key = os.getenv("OPENAI_API_KEY")  # Certifique-se de que a variável de ambiente está definida
client = OpenAI(api_key=api_key)
