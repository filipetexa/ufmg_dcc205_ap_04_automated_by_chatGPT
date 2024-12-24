import os
import subprocess
from openai import OpenAI # Instale a biblioteca usando 'pip install openai'

# Configuração da API OpenAI
api_key = os.getenv("OPENAI_API_KEY")
# Caminhos e extensões
reference_directory = "src"  # Diretório de referência com arquivos .c


bin_directory = os.path.join(reference_directory, "bin")
os.makedirs(bin_directory, exist_ok=True)  # Cria a pasta bin se não existir

# Função para buscar arquivos .c
def find_c_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".c")]

# Função para compilar usando GDB
def compile_with_gdb(c_file_path, output_name):
    subprocess.run(["gcc", "-g", c_file_path, "-o", output_name])

# Função para rodar o Valgrind e coletar a saída
def run_valgrind(executable_path):
    valgrind_command = [
        "valgrind",
        "--leak-check=full",           # Verifica vazamentos de memória
        "--show-leak-kinds=all",       # Mostra todos os tipos de vazamentos
        "--track-origins=yes",         # Rastreia a origem dos erros de valor não inicializado
        "--verbose"                    # Saída detalhada
    ]
    
    try:
        # Executa o comando Valgrind com timeout de 10 segundos
        result = subprocess.run(valgrind_command + [executable_path], capture_output=True, text=True, timeout=10)
        return result.stdout
    except subprocess.TimeoutExpired:
        # Se o Valgrind ultrapassar 10 segundos, retorna uma mensagem informativa
        return "essa função não teve resultado no valgrind"


# Função para enviar prompt para API ChatGPT e receber a resposta
def send_to_chatgpt(prompt):

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Especifique o modelo desejado
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()


# Função principal para processar cada arquivo .c
def process_files(directory):
    c_files = find_c_files(directory)
    for c_file in c_files:
        c_file_path = os.path.join(directory, c_file)
        executable_path = os.path.join(bin_directory, c_file.replace(".c", ""))
        
        # Passo 2: Compilar o arquivo
        compile_with_gdb(c_file_path, executable_path)
        
        # Passo 3 e 4: Rodar Valgrind e coletar resposta
        valgrind_output = run_valgrind(executable_path)
        
        # Passo 5: Criar o prompt para o ChatGPT
        prompt = f"""
        Analise o seguinte código C e identifique os problemas. Em seguida, forneça apenas o código corrigido com comentários nas linhas onde houve alterações e uma explicação separada sobre as correções realizadas.

        Código:
        {open(c_file_path).read()}

        Saída do Valgrind:
        {valgrind_output}

        Responda em português. Separe o código corrigido e a explicação da correção com o separador "=====break=====".
        """

        
        # Enviar para a API ChatGPT e receber a resposta
        response_text = send_to_chatgpt(prompt)
        
        # Passo 6: Separar a resposta em código e explicação
        parts = response_text.split("=====break=====")
        if len(parts) == 2:
            corrected_code, explanation = parts
        else:
            corrected_code, explanation = response_text, "Erro ao separar a resposta."
        
        # Salvar o código corrigido e o relatório
        corrected_file_path = os.path.join(directory, f"{c_file.replace('.c', '')}_correto.c")
        report_file_path = os.path.join(directory, f"{c_file.replace('.c', '')}_relatorio.txt")
        
        with open(corrected_file_path, "w") as corrected_file:
            corrected_file.write(corrected_code.strip())
        
        with open(report_file_path, "w") as report_file:
            report_file.write(explanation.strip())

# Executar o processo
process_files(reference_directory)
