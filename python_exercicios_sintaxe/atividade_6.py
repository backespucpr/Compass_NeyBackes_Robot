#Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x 
#e apresenta os impares entre 0 e x


#função que recebe o valor digitiado maior de 2
def informeValor():
  valor = int(input('Informe um valor maior que 2? '));
  return recebeValor(valor);

#funçao que verifica o valor e informa os valores pares de 0 ao valor X 
def recebeValor(valor):
  valores = []
  for i in range(1, valor):
    if i % 2 == 1:
      valores.append(i)
  return f'Estes são os números impares entre 0 e {valor}: {valores}'


#chamada da função que inicia o programa
print(informeValor())