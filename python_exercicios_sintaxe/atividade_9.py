#Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre
# os valores da lista do ultimo para o primeiro


#sendo junto, vamos solicitar a quantidade de valores para a lista : )
entrada = int(input('Quantos valores gostaria de armazenar?'));
#inicilizando uma lista vazia que vai receber os nossos valores
lista = []
#usando o for com o range entrada para determinar a quantidade valores a ser inserido na lista
for value in range(1, entrada + 1):
    valor = int(input(f'Informe {value} valor: '));
    lista.append(valor)

#imprimindo a lista ao contrário
print(lista[::-1])