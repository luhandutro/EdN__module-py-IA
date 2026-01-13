
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 02
#=======================================================================


"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

RS_US = 5.2
RS_EU = 6.15
default_value = 100

d_v_US = round((default_value/RS_US),2)
d_v_EU = round((default_value/RS_EU),2)

print("-----------------------")
print("Questão [1] - Resposta:")
print("|")
print("R$ 100 equivale a US$ " + str(d_v_US) + " (dólares), e também a € " + str(d_v_EU) + " (euros).")



"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

prod_name = "Camiseta"
price_camst = 50
desc_camst = 0.2*price_camst
price_desc_camst = price_camst - desc_camst

print("-----------------------")
print("Questão [2] - Resposta:")
print("|")
print("Produto: " + prod_name)
print("Preço original: R$ " + f"{price_camst:.2f}".replace('.', ','))
print("Desconto: R$ " + f"{desc_camst:.2f}".replace('.', ',') + " (20%)")
print("Preço final: R$ " + f"{price_desc_camst:.2f}".replace('.', ','))



"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

nota1 = 7.5
nota2 = 8
nota3 = 6.5
nota_f = (nota1 + nota2 + nota3)/3

print("-----------------------")
print("Questão [3] - Resposta:")
print("|")
print("Nota 1: " + f"{nota1:.2f}".replace('.', ','))
print("Nota 2: " + f"{nota2:.2f}".replace('.', ','))
print("Nota 3: " + f"{nota3:.2f}".replace('.', ','))
print("NOTA FINAL: " + f"{nota_f:.2f}".replace('.', ','))



"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
incluindo o resultado final arredondado para duas casas decimais."""

dist_perc = 300
comb_gast = 25

consum_Lpkm = comb_gast/dist_perc
dist_kmpL = dist_perc/comb_gast

print("-----------------------")
print("Questão [4] - Resposta:")
print("|")
print("Distância percorrida: " + str(dist_perc) + " km")
print("Combustível gasto: " + str(comb_gast) + " L")
print("Consumo médio de litros por quilômetro percorrido (L/km) : " + f"{consum_Lpkm:.2f}".replace('.', ',') + " L/km")
print("Distância média percorrida para cada litro consumido (km/L) : " + f"{dist_kmpL:.2f}".replace('.', ',') + " km/L")
print("-----------------------")




print("----------------------- [1] & [3]: input ---------------- ")
print("Questão [1] - input:")
print("|")
new_value = input("Digite um novo valor em reais (R$) para conversão em dólar (US$) e euro (€): ")
new_value = float(new_value)
n_v_US = round((new_value/RS_US),2)
n_v_EU = round((new_value/RS_EU),2)
print("R$ " + f"{new_value:.2f}".replace('.', ',') + " = US$ " + str(n_v_US) + " = € " + str(n_v_EU))

print("-----------------------")
print("Questão [3] - input:")
print("|")
print("Digite as 3 notas do aluno:")
new_not1 = input(); new_not1 = float(new_not1)
new_not2 = input(); new_not2 = float(new_not2)
new_not3 = input(); new_not3 = float(new_not3)
new_notf = (new_not1 + new_not2 + new_not3)/3
print("|")
print("Nota 1: " + f"{new_not1:.2f}".replace('.', ','))
print("Nota 2: " + f"{new_not2:.2f}".replace('.', ','))
print("Nota 3: " + f"{new_not3:.2f}".replace('.', ','))
print("NOTA FINAL: " + f"{new_notf:.2f}".replace('.', ','))