
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 03
#=======================================================================

"""1- Classificador de Idade
|||
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais)."""

print("-----------------------")
print("Questão [1]:")
print("|")
idade_user = input("Qual é a sua idade? ")
idade_user = abs(float(idade_user)) #\_caso o usuário digite acidentalmente um valor negativo, o mesmo será convertido para positivo

if idade_user < 13:
    print("Você é uma criança!")
elif idade_user < 18:
    print("Você ainda é adolescente...")
elif idade_user < 60:
    print("Você é adulto(a)!")
else:
    print("Já és idoso(a)!")



"""2- Calculadora de IMC
|||
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso" """

print("-----------------------")
print("Questão [2]:")
print("|")
massa = input("Digite seu peso (kg): ")
massa = abs(float(massa)) #\_caso o usuário digite acidentalmente um valor negativo, o mesmo será convertido para positivo

altura = input("Digite sua altura, em metros: ")
altura = float(altura)

IMC = massa/(altura**2)

print("O seu Índice de Massa Corporal (IMC) é de " + f"{IMC:.2f}".replace('.', ',') + " kg/m²")

if IMC < 18.5:
    print("Classificação: Abaixo do peso")
elif IMC < 25:
    print("Classificação: Peso normal")
elif IMC < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")



"""3- Conversor de Temperatura
|||
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

print("-----------------------")
print("Questão [3]:")
print("|")
Temper_i = input("Valor da temperatura a ser convertida: ")
Temper_i = float(Temper_i)

print("Unidades de Temperatura: digite K para Kelvin, C para Celsius e F para Fahrenheit")

unidad_orig_T = input("Unidade de origem: ")
unidad_orig_T = unidad_orig_T.upper()

unidad_final_T = input("Unidade final: ")
unidad_final_T = unidad_final_T.upper()

if unidad_orig_T == 'K' and unidad_final_T == 'C':
    Temper_f = Temper_i - 273.15
    print(str(Temper_i) + " K = " + str(Temper_f) + " °C")
elif unidad_orig_T == 'C' and unidad_final_T == 'K':
    Temper_f = Temper_i + 273.15
    print(str(Temper_i) + " °C = " + str(Temper_f) + " K")
elif unidad_orig_T == 'K' and unidad_final_T == 'F':
    Temper_f = 1.8*(Temper_i - 273.15) + 32
    print(str(Temper_i) + " K = " + str(Temper_f) + " °F")
elif unidad_orig_T == 'F' and unidad_final_T == 'K':
    Temper_f = (Temper_i - 32)/1.8 + 273.15
    print(str(Temper_i) + " °F = " + str(Temper_f) + " K")
elif unidad_orig_T == 'C' and unidad_final_T == 'F':
    Temper_f = 1.8*Temper_i + 32
    print(str(Temper_i) + " °C = " + str(Temper_f) + " °F")
elif unidad_orig_T == 'F' and unidad_final_T == 'C':
    Temper_f = (Temper_i - 32)/1.8
    print(str(Temper_i) + " °F = " + str(Temper_f) + " °C")
elif unidad_orig_T == unidad_final_T:
    Temper_f = Temper_i
    print(str(Temper_i) + " " + str(unidad_orig_T) + " = " + str(Temper_f) + " " + str(unidad_final_T))
else:
    print("Unidade(s) de medida inválida!")

#C = K - 273.15
#K = C + 273.15
#F = 1.8*(K - 273.15) + 32
#K = (F - 32)/1.8 + 273.15
#F = 1.8*C + 32
#C = (F - 32)/1.8



"""4- Verificador de Ano Bissexto
|||
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400."""

print("-----------------------")
print("Questão [4]:")
print("|")
year = input("Digite o ano: ")
year = abs(int(float(year))) #\_caso o usuário digite acidentalmente um valor negativo, o mesmo será convertido para positivo

if (year % 4) != 0:
   print("O ano não é múltiplo de 4, então não é bissexto.")
elif (year % 4) == 0 and (year % 100) != 0:
   print("O ano É BISSEXTO, porque é múltiplo de 4 e não é múltiplo de 100.")
elif (year % 100) == 0 and (year % 400) != 0:
   print("Especialmente, o ano NÃO É BISSEXTO, pois apesar de ser múltiplo de 4, é um centenário não múltiplo de 400.")
elif (year % 400) == 0:
   print("O ano É ESPECIALMENTE BISSEXTO, pois é um centenário múltiplo de 400.")

print("-----------------------")