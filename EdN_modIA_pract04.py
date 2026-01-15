
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 04
#=======================================================================

"""1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso."""

print("-----------------------")
print("Questão [1]:")
print("|")

basic_operators = ["+", "-", "*", "/"]

pwhil = 0
while pwhil == 0:
    try:
        numr1 = float(input("Digite o primeiro número: "))
        print(numr1)
        print("___")
        pwhil = pwhil + 1
    except ValueError:
        print("Entrada inválida! Insira apenas um valor numérico.")


pwhil = 0
while pwhil == 0:
    operador12 = input("Selecione a operação (+, -, *, /): ")
    if operador12 in basic_operators:
        print(operador12)
        print("___")
        pwhil = pwhil + 1
    else:
        print("Operador inválido! Tente novamente.")


pwhil = 0
while pwhil == 0:
    try:
        numr2 = float(input("Digite o segundo número: "))
        print(numr2)
        if (operador12 != basic_operators[3]) or (numr2 != 0):
            print("___")
            pwhil = pwhil + 1
        else:
            prop_error = 1/numr2 #\__erro proposital (divisão por zero)
    except ValueError:
        print("Entrada inválida! Insira apenas um valor numérico.")
    except ZeroDivisionError:
        print("Resultado inválido! Não é possível dividir por zero! Insira um valor diferente de zero.")


if operador12 == basic_operators[0]:
    result_oper = numr1 + numr2
elif operador12 == basic_operators[1]:
    result_oper = numr1 - numr2
elif operador12 == basic_operators[2]:
    result_oper = numr1 * numr2
elif operador12 == basic_operators[3]:
    result_oper = numr1 / numr2

print(str(numr1) + " " + operador12 + " " + str(numr2) + " = ")
print("Resultado: " + str(result_oper))



"""2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro."""

print("-----------------------")
print("Questão [2]:")
print("|")

notas_somadas = 0.0
quant_alunos = 0

while True: #\__loop infinito até que o comando 'break' seja executado
    entrada_user = input("Digite uma nota entre 0 e 10 (ou 'fim' para encerrar): ")

    if entrada_user.lower() == "fim": #\__não importa se há letras maiúsculas na entrada
        break

    try:
        nota = float(entrada_user)
    except ValueError:
        print("Erro: entrada inválida. Digite um número ou 'fim'.")
        continue

    if nota < 0 or nota > 10:
        print("Erro: a nota deve estar entre 0 e 10.")
    else:
        notas_somadas += nota
        quant_alunos += 1

print("_______")
if quant_alunos > 0:
    media_turma = notas_somadas / quant_alunos
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Total de notas válidas: {quant_alunos}")
else:
    print("Nenhuma nota válida foi registrada.")



"""3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair"."""

print("-----------------------")
print("Questão [3]:")
print("|")

while True:
    senha_user = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha_user.lower() == "sair": #\__não importa se há letras maiúsculas na entrada
        print("Programa encerrado pelo usuário.")
        break

    tem_numero = False
    tem_nao_numerico = False

    for caractere in senha_user:
        if caractere.isdigit(): #\__isdigit() verifica se o caractere é numérico
            tem_numero = True
        else:
            tem_nao_numerico = True

    if len(senha_user) >= 8 and tem_numero and tem_nao_numerico:
        print("_____")
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.")



"""4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas."""

print("-----------------------")
print("Questão [4]:")
print("|")

quant_par = 0
quant_impar = 0

while True:
    n_user = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if n_user.lower() == "fim":
        break

    try:
        numero = int(n_user)
    except ValueError:
        print("Erro: entrada inválida. Digite apenas números inteiros.")
        continue

    if numero % 2 == 0:
        print(f" {numero} é um número par.")
        quant_par += 1
    else:
        print(f" {numero} é um número ímpar.")
        quant_impar += 1

print("___")
print(f"Quantidade de números pares: {quant_par}")
print(f"Quantidade de números ímpares: {quant_impar}")