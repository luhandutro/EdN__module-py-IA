
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 06
#=======================================================================

print("-----------------------")
"""1 - Crie um programa que gere senhas aleatórias com o módulo random, utilizando letras, números e símbolos (caracteres especiais),
de modo que o usuário possa escolher o tamanho da senha para criar senhas seguras automaticamente."""

print("Questão [1]:")
print("|")

import random

# Conjuntos de caracteres
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+[]{};:,.<>?/\|¨~"

# Solicitar o tamanho da senha
entr_user = input("Digite o número de caracteres da senha (no mínimo 8): ")

# Validar a entrada
try:
    num_caract = int(entr_user)
    if num_caract < 8:
        raise ValueError
except ValueError:
    print("Entrada inválida. A senha será gerada com um tamanho aleatório entre 8 e 16 caracteres.")
    num_caract = random.randint(8, 16)

# Garantir pelo menos um caractere de cada tipo
senha = [random.choice(letras), random.choice(numeros), random.choice(simbolos)] #\__ até aqui, apenas 3 caracteres são gerados

# Completar o restante da senha
todos_os_caracteres = letras + numeros + simbolos
for _ in range(num_caract - 3):
    senha.append(random.choice(todos_os_caracteres)) #\__em cada iteração, há um incremento de caractere aleatório na senha

# Embaralhar os caracteres (para que os primeiros 3 caracteres não sejam necessariamente uma sequência de letra, número e símbolo)
random.shuffle(senha)

# Converter a lista de strings em uma única string ('senha' é lista, e 'senha_final' é string)
senha_final = "".join(senha)

# Exibir a senha gerada
print(f"Senha gerada ({num_caract} caracteres): {senha_final}")




print("-----------------------")
"""2 - Crie um programa que acesse a API Random User Generator para buscar um usuário fictício aleatório,
exibindo o nome, e-mail e país desse usuário. Caso houver erro na conexão, mostre uma mensagem de falha."""

print("Questão [2]:")
print("|")

# python -m pip install requests #\___ Máquina local (VS Code, PowerShell, CMD, Terminal)
# pip install requests #\_____________ Jupyter Notebook / Google Colab
# %pip install requests #\____________ Jupyter Notebook / Google Colab
# pip3 install requests #\____________ mais comum em: Linux / macOS

import requests

def buscar_randomuser():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)

        # Verificar se a resposta foi bem-sucedida (status code 200)
        if resposta.status_code != 200:
            print("Falha ao acessar a API.")
            return

        dados = resposta.json()

        usuario = dados["results"][0]

        nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
        idade = usuario["dob"]["age"]
        email = usuario["email"]
        pais = usuario["location"]["country"]

        endereco = (
            f'{usuario["location"]["street"]["name"]}, '
            f'{usuario["location"]["street"]["number"]} - '
            f'{usuario["location"]["city"]}'
        )

        print("Usuário fictício encontrado:\n")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print(f"Endereço: {endereco}")

    except requests.exceptions.RequestException:
        print("Erro de conexão com a API.")


# Chamando a função para apresentar informações de um usuário aleatório
buscar_randomuser()




print("-----------------------")
"""3 - Crie um programa que consulte informações de um CEP na API ViaCEP,
retornando logradouro, bairro, cidade e estado correspondentes ao CEP informado pelo usuário.
Caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha."""

print("Questão [3]:")
print("|")

# python -m pip install requests #\___ Máquina local (VS Code, PowerShell, CMD, Terminal)
# pip install requests #\_____________ Jupyter Notebook / Google Colab
# %pip install requests #\____________ Jupyter Notebook / Google Colab
# pip3 install requests #\____________ mais comum em: Linux / macOS

import requests

def consultar_cep(cep):
    """
    Consulta um CEP na API ViaCEP e retorna os dados do endereço.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  #\__ Gera erro se o status HTTP não for 200

        dados = resposta.json()

        # Verificar se o CEP inexiste
        if "erro" in dados:
            return None

        return {
            "logradouro": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
        }

    except requests.exceptions.RequestException:
        return None

# -------------------------------

cep_usuario = input("Digite o CEP (apenas números): ").strip()

# Validação simples do CEP
if not cep_usuario.isdigit() or len(cep_usuario) != 8:
    print("[!] CEP inválido. Digite exatamente 8 números.")
else:
    resultado = consultar_cep(cep_usuario)

    if resultado is None:
        print("[!] Falha na consulta. CEP não encontrado ou erro na requisição.")
    else:
        print("\nEndereço encontrado:")
        print(f"- Logradouro: {resultado['logradouro']}")
        print(f"- Bairro: {resultado['bairro']}")
        print(f"- Cidade: {resultado['cidade']}")
        print(f"- Estado: {resultado['estado']}")




print("-----------------------")
"""4 - Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
O usuário deve informar o código da moeda desejada (exemplo: USD, EUR, GBP) e o programa deve exibir
o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
Utilize a API da AwesomeAPI para obter os dados de cotação.
Caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro."""

print("Questão [4]:")
print("|")

# python -m pip install requests #\___ Máquina local (VS Code, PowerShell, CMD, Terminal)
# pip install requests #\_____________ Jupyter Notebook / Google Colab
# %pip install requests #\____________ Jupyter Notebook / Google Colab
# pip3 install requests #\____________ mais comum em: Linux / macOS

import requests

def consult_cotacao():
    moeda = input("Informe o código da moeda (ex: USD, EUR, GBP, JPY, RUB): ").upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status() #\__ Gera erro se o status HTTP não for 200

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Erro: moeda não encontrada ou código inválido.")
            return

        cotacao = dados[chave]

        valor_atual = float(cotacao["bid"])
        valor_maximo = float(cotacao["high"])
        valor_minimo = float(cotacao["low"])
        data_hora = cotacao["create_date"]

        print("\nCotação da moeda em R$ (BRL)")
        print(f"- Moeda: {moeda}")
        print(f"- Valor atual: R$ {valor_atual:.4f}")
        print(f"- Máximo do dia: R$ {valor_maximo:.4f}")
        print(f"- Mínimo do dia: R$ {valor_minimo:.4f}")
        print(f"- Última atualização: {data_hora}")

    except requests.exceptions.HTTPError:
        status = resposta.status_code

        if status == 429:
            print("\n[!] Erro HTTP 429: Too Many Requests --- A API bloqueou temporariamente esta requisição.")
            print("\nPossíveis motivos:")
            print("- O endereço IP do ambiente é compartilhado (ex: Google Colab)")
            print("- O limite de requisições da API gratuita foi atingido")
            print("\nSugestões:")
            print("- Tente novamente mais tarde")
            print("- Execute o código localmente (VS Code)")
        elif status == 404:
            print("\n[!] Erro HTTP 404: Endpoint ou moeda não encontrada.")
        else:
            print(" ")
            print(f"[!] Erro HTTP inesperado: código {status}")

    except requests.exceptions.Timeout:
        print("\n[!] Erro: tempo limite da requisição excedido.")

    except requests.exceptions.ConnectionError:
        print("\n[!] Erro: não foi possível conectar ao servidor da API.")

    except requests.exceptions.RequestException as e:
        print(" ")
        print(f"[!] Erro inesperado na requisição: {e}")

    except Exception as e:
        print(" ")
        print(f"[!] Erro inesperado no programa: {e}")


# Chamando a função para solicitar o código da moeda e apresentar a cotação
consult_cotacao()

print("-----------------------")