#Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x
#e apresenta os impares entre 0 e x

#função reutilizada da atividade 2
def media(a,b):
  media = (a + b) / 2
  return f'A media entre os dois valores: {media}';


#variáves para receber as valores
valor1 = float(input('Informa o primeiro valor: '));
valor2 = float(input('Informe o segundo valor: '));

#imprimtir o resultado utilizando a função media
print(media(valor1, valor2));