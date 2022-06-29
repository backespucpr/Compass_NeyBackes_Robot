#Crie um programa que recebe uma lista com três frutas e 
#compare com uma lista com os valores ["maça", "banana", "pera"]

lista = ["maça", "banana", "pera"]

#lista vazia e uma laço for para pegar as frutas do usuário
lista1 = []
for value in range(1, 4):
    valor = str(input(f'Informe a {value} fruta: '));
    lista1.append(valor)
#versão enxuta para comparar os valores das duas listas
comparar = [fruta for fruta in lista if fruta in lista1]

#verificando se existe algo na lista comparar 
if len(comparar) == 0:
    print('Não existe frutas repetidas nas duas listas')
else:
    print(f'{comparar} estas são as frutas repetidas nas duas listas.')




    