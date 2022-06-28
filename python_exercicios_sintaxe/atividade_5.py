#Construa um programa que recebe 20 valores para X e 
#no final apresenta a média aritmética dos valores pares digitados

def recebe_valor():
  valores = []
  for i in range(20):
    valor = float(input('Informe um valor: '));
    i += 1    
    valores.append(valor)
  return(media_pares(valores))
  
def media_pares(valores):  
  div = 0
  par = 0
  for value in valores:
    if (value % 2 == 0):
      par +=value;
      div += 1;      
  return f'Entre 1 e 20 temos {div} pares e a media aritmética entres esses números é {(par // div)}'  
    
print(recebe_valor())