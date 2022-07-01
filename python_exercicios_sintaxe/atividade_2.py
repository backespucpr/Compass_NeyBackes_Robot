#Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre eles.

#função para calcular a média
def media(a,b):
  media = (a + b) / 2
  return f'A media entre as duas notas é: {media}';

#variáves para receber as notas
nota1 = float(input('Informa a primeira nota: '));
nota2 = float(input('Informe a segunda nota : '));

#imprimtir o resultado utilizando a função media
print(media(nota1, nota2));