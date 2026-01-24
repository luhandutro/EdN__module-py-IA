
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 07
#=======================================================================

print("-----------------------")
"""1 - ___Escrita de Arquivo CSV___
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:
* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.
* Trate possíveis erros de escrita de arquivo.
|
Dica: Use `csv.writer()` para escrever os dados linha por linha."""

print("Questão [1]:")
print("|")

import csv
from pathlib import Path

# ------ Detectar o ambiente (Google Colab ou não) ----------
def em_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

# -------------- Definir o diretório base -------------------
if em_colab():
    base_dir = Path("/content")
    ambiente = "Google Colab"
else:
    base_dir = Path(__file__).resolve().parent
    ambiente = "Máquina local (VS Code / Windows)"

# ----------------- Pasta para os CSVs ----------------------
#pasta_csv = base_dir / "dados_csv"
#pasta_csv.mkdir(exist_ok=True)

# ------------------ Dados fictícios ------------------------
pessoas = [
    ["Januário", 52, "Rio de Janeiro/RJ"],
    ["Janira", 48, "Jaru/RO"],
    ["Julio", 35, "Juara/MT"],
    ["Augusto", 23, "Augustinópolis/TO"]
]

# ------------------ Nome do arquivo ------------------------
nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoasbr1.csv): ").strip()
#caminho_arquivo = pasta_csv / nome_arquivo
caminho_arquivo = base_dir / nome_arquivo

# ------------------ Escrita do CSV -------------------------
try:
    with caminho_arquivo.open("w", newline="", encoding="utf-8") as arq_csv:
        escritor_csv = csv.writer(arq_csv)
        escritor_csv.writerow(["Nome", "Idade", "Cidade"])
        for person in pessoas:
            escritor_csv.writerow(person)

    print(f"O arquivo '{nome_arquivo}' foi gravado com sucesso!")
    print("Ambiente:", ambiente)
    print("Local:", caminho_arquivo)

except PermissionError as e:
    print("Erro de permissão ao escrever o arquivo.")
    print(e)

except OSError as e:
    print("Erro no sistema de arquivos.")
    print(e)




print("-----------------------")
"""2 - ___Leitura de Arquivo CSV___
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:
* Solicite ao usuário o nome do arquivo CSV a ser lido.
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.
* Exiba cada linha completa como uma lista.
* Trate erros como arquivo inexistente ou problemas na leitura, mostrando uma mensagem de erro.
|
Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo."""

print("Questão [2]:")
print("|")

import csv
from pathlib import Path

# -------------- Detectar o ambiente (Google Colab ou não) ------------------
def em_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

# --- Definir o diretório base (onde estão o script .py e o arquivo .csv) ---
if em_colab():
    base_dir = Path("/content")
    ambiente = "Google Colab"
else:
    base_dir = Path(__file__).parent
    ambiente = "Máquina local (VS Code / Windows)"


# ------------------ Definir a função de leitura CSV ------------------------
def ler_arquivo_csv():
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: dados.csv): ")

    # Caminho completo do arquivo CSV
    caminho_arquivo = base_dir / nome_arquivo

    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arq_csv:
            leitor_csv = csv.reader(arq_csv)

            print("\nConteúdo do arquivo CSV:\n")
            for linha in leitor_csv:
                print(linha)

    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado na mesma pasta do script.")
    except PermissionError:
        print("Erro: você não tem permissão para acessar este arquivo.")
    except Exception as erro:
        print(f"Ocorreu um erro ao ler o arquivo: {erro}")

# Chamando a função para ler o arquivo CSV
ler_arquivo_csv()




print("-----------------------")
"""3 - ___Leitura e Escrita de Arquivo JSON___
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:
* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
* Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.
* Trate possíveis erros como ausência do arquivo ou problemas na escrita, mostrando uma mensagem de falha.
|
Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo."""

print("Questão [3]:")
print("|")

import json
from pathlib import Path

# -------------- Detectar o ambiente (Google Colab ou não) -------------------
def em_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

# --- Definir o diretório base (onde estão o script .py e o arquivo .json) ---
if em_colab():
    base_dir = Path("/content")
    ambiente = "Google Colab"
else:
    base_dir = Path(__file__).resolve().parent
    ambiente = "Máquina local (VS Code / Windows)"

# ------------ Criação dos dicionários (cada um para uma pessoa) -------------
pessoajs = [
    {
        "nome": "Ubirajara",
        "idade": 56,
        "cidade": "Araraquara/SP"
    },
    {
        "nome": "Bartolomeu",
        "idade": 50,
        "cidade": "Blumenau/SC"
    },
    {
        "nome": "Zenóbio",
        "idade": 47,
        "cidade": "Oiapoque/AP"
    },
    {
        "nome": "Zilda",
        "idade": 45,
        "cidade": "Belo Horizonte/MG"
    }
]

# Solicitar o nome do arquivo JSON ao usuário
nome_arquivojs = input("Digite o nome do arquivo JSON (ex: dadosXYZ.json): ")

# Definir o caminho (path) do arquivo JSON
caminho_arquivojs = base_dir / nome_arquivojs

# Salvar os dicionários no arquivo JSON
try:
    with open(caminho_arquivojs, "w", encoding="utf-8") as arqjs:
        json.dump(pessoajs, arqjs, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso!")
except IOError:
    print("Erro ao salvar o arquivo JSON.")

# Ler o arquivo JSON salvo
try:
    with open(caminho_arquivojs, "r", encoding="utf-8") as arqjs:
        dadojs_lidos = json.load(arqjs)
    print("\nDados lidos do arquivo:")
    print(dadojs_lidos)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")
except IOError:
    print("Erro ao ler o arquivo.")


print("-----------------------")