#Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores

#função reutilizada da atividade 2
def media(a,b):
  media = (a + b) / 2
  return f'A media entre os dois valores: {media}';


#variáves para receber as valores
valor1 = float(input('Informa o primeiro valor: '));
valor2 = float(input('Informe o segundo valor: '));

#imprimir o resultado utilizando a função media
print(media(valor1, valor2));