
# Lucas I. D. Castro (luhandutro)

# EdN BRSAO_210 - AWS re/Start 2 - Módulo IA _-_-_ atividade prática 05
#=======================================================================

"""[1] Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""

print("-----------------------")
print("Questão [1]:")
print("|")

gorjeta = lambda conta_rest, porc_gorj: conta_rest*porc_gorj/100

# print("Para calcular a gorjeta, utilize a função 'gorjeta(x,y)', sendo x o valor da conta e y a porcentagem (%)")

xcont = float(input("Valor total da conta: "))
yporc = float(input("Porcentagem da gorjeta (%): "))
z_grj = gorjeta(xcont,yporc)
print("__")
print("O valor da gorjeta é: ")
print(z_grj)




"""[2] Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

print("-----------------------")
print("Questão [2]:")
print("|")

import unicodedata

def palindromia(texto):
    text_padroniz = "" #\__texto inicialmente vazio e crescente com caracteres padronizados

    for caractere in texto.lower(): #\__".lower()" transforma as letras maiúsculas em minúsculas
        # Padronizar o caractere da iteração (separar letra e acento, se aplicável, e em seguida eliminar o acento)
        caract_minus_s_acent = unicodedata.normalize('NFD', caractere) #\__'NFD' separa letra e acento, se aplicável
        caract_minus_s_acent = ''.join(c for c in caract_minus_s_acent if unicodedata.category(c) != 'Mn')
        #_\_ caract_minus_s_acent se transforma em vazio e reaproveita apenas o caractere que não seja 'Mn' (Mark, Nonspacing)

        # Manter letras e números
        if caract_minus_s_acent.isalnum(): #\__ só retorna True se o caractere for alfanumérico (letra ou número)
            text_padroniz += caract_minus_s_acent #\__ o texto padronizado não recebe espaços nem pontuações

    # Verificação de palindromia
    if text_padroniz == text_padroniz[::-1]: #\__ Verifica se o texto é igual ao seu inverso
        return "Sim, o texto é um palíndromo!"
    else:
        return "Não, não é palíndromo..."


frase_alfanum = input("Digite uma palavra, um número ou uma frase: ")
result_palin = palindromia(frase_alfanum)
print(result_palin)

#] Para testes:
#
# z&|7301--Socorram-me!! Subi nò ônibus êm Màrróços +* 1037 z
# z&|7301--Socorram-me!! Subi nò ônibus êm Màrróços +* 1037 y




"""[3] Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado."""

print("-----------------------")
print("Questão [3]:")
print("|")

def reduzir_preco(preco, percent):
    descont = preco*(percent/100)
    preco_final = preco - descont
    #preco_final = round(preco_final, 2)
    return preco_final

preco_user = float(input("Digite o preço do produto (R$): "))
percent_user = float(input("Digite o percentual de desconto (%): "))

prec_fin = reduzir_preco(preco_user, percent_user) #\__ prec_fin = preco_final

print("Preço final com desconto: R$ " + f"{prec_fin:.2f}".replace('.', ','))




"""[4] Crie um programa que calcule há quantos dias um individuo está vivo de acordo com a data do dia.
#
#\__ Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

print("-----------------------")
print("Questão [4]:")
print("|")

def converter_p_dias(dia, mes, ano):
    # return (ano * 365) + (mes * 30) + dia #\___menos preciso do que o modelo abaixo
    return (ano * 365.25) + (mes * 30.4375) + dia #\___mais preciso, embora não exato

# Data de nascimento
dia_nasc = int(input("Digite o dia de nascimento: "))
mes_nasc = int(input("Digite o mês de nascimento: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

# Data atual
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

# Conversão
data_nascimento = converter_p_dias(dia_nasc, mes_nasc, ano_nasc)
data_atual = converter_p_dias(dia_atual, mes_atual, ano_atual)

idade_em_dias = round(data_atual - data_nascimento)

print("Sua idade aproximada em dias é:", idade_em_dias)

print("-----------------------")