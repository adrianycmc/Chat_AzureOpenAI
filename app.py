import openai
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar as chaves de API e o endpoint do Azure usando variáveis de ambiente
openai.api_type = os.getenv("AZURE_OPENAI_API_TYPE")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_API_BASE")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

def chat_openai(prompt):
    try:
        resposta = openai.Completion.create(
            engine="pychat-gpt", 
            prompt=prompt,
            max_tokens=100,  
            n=1,
            stop=["\n", "Pergunta:"], 
            temperature=0.5
        )
        return resposta.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao se comunicar com o Azure OpenAI: {e}"

def main():
    print("Bem-vindo ao Chatbot! O que quer saber hoje? 👽")
    
    system_prompt = f"""
    Você é um assistente útil e informativo. Forneça respostas claras e concisas às perguntas dos usuários. 
    Caso o usuário pergunte quem é você, responda: 'Oi, eu sou a ajudante da Adriany!'
    Considere o ano de 2024 para responder sobre atualidades.
    """

    while True:
        user_input = input("➡️ : ")
        if user_input.lower() in ['sair', 'exit']:
            print("🤖 : Até mais! 👋 ")
            break
        
        prompt = f"{system_prompt}\n\nPergunta: {user_input}\nResposta:"
        responsta = chat_openai(prompt)

        limpar_responsta = responsta.split('\n')[0].strip()
        print("🤖:", limpar_responsta)

if __name__ == "__main__":
    main()


