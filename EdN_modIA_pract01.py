"""1- Programa de Saudação
* Crie um programa que imprima a mensagem "Olá, mundo!" na tela."""

print("-----------------------")
print("Questão [1] - Resposta:")
print("|")
print("Olá, mundo!")
print("Hello world, heavy world!!!")



"""2- Calculadora de Soma
* Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14.
O programa deve calcular a soma e exibir o resultado."""

numero1 = 12
numero2 = 14

sum_numbers = numero1 + numero2

print("-----------------------")
print("Questão [2] - Resposta:")
print("|")
print("A soma dos números é igual a " + str(sum_numbers))



"""3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³."""

compr_box = 12
larg_box = 14
alt_box = 20

volume_box = compr_box*larg_box*alt_box

print("-----------------------")
print("Questão [3] - Resposta:")
print("|")
print("O volume da caixa é de " + str(volume_box) + " cm³" + " (= " + str(volume_box) + " mL)")



"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

prod_name = "Cadeira Infantil"
price_chair = 12.4
quant_chair = 3

total_cost = price_chair*quant_chair
reais_tot_c = int(total_cost)
centavos_toc_c = int(100*(total_cost - reais_tot_c))

print("-----------------------")
print("Questão [4] - Resposta:")
print("|")
print("Produto: " + prod_name)
print("Preço unitário: R$ " + str(int(price_chair)) + "," + str(int(100*(price_chair - int(price_chair)))))
print("Quantidade: " + str(quant_chair))
print("Custo total da compra: R$ " + str(reais_tot_c) + "," + str(centavos_toc_c))
print("-----------------------")