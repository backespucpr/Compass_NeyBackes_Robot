#Construa um programa que recebe 20 valores para X e 
#no final apresenta a média aritmética dos valores pares digitados

#a primeira função chama a entrada de dados que será armazenado em uma lista
def recebeValor():
  valores = []
  for i in range(20):
    valor = float(input('Informe um valor: '));
    i += 1    
    valores.append(valor)
  return(mediaPares(valores))

# a função media_pares recebe como paramêtro os valores salvos na lista valores e verifica os valores pares
def mediaPares(valores):  
  div = 0
  par = 0
  for value in valores:
    if (value % 2 == 0):
      par +=value;
      div += 1;      
  return f'Entre 1 e 20 temos {div} pares e a media aritmética entres esses números é {(par // div)}'  
    
#imprimtir o resultado utilizando o print para iniciar a fumção que recebe os valores  
print(recebeValor())