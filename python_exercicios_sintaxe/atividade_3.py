#Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

#função que soma valores e indentifica o resultado como par ou impar
def par_impar(a,b):
  soma = a + b;
  
  if (soma % 2 == 0):
  #trabalhando com um novo formato de impressão  
    return f"O soma do número {a} com o número {b} é igual a {soma}, que é um número par";
  return f"O soma do número {a} com o número {b} é igual a {soma}, que é um número impar";

#variáves para receber as notas
num1 = int(input('Inform o primeiro número: '));
num2 = int(input('informe o segundo número: '));

#imprimtir o resultado utilizando a função par_impar
print(par_impar(num1,num2));
