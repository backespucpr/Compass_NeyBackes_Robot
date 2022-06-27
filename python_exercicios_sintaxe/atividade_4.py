#Construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, 
# apresenta "Maior de idade", se a idade for menor que 12, apresenta "Você é uma criança"
# e se for maior que 12 e menor que 18, apresenta "Você é um adolescente".


#Função para comparar a idade
def maior_idade(a):
  if (a > 18):
    return f"Sua idade é {a}. Maior de idade";
  elif (a < 12):
    return f"Sua idade é {a}.Você é uma criança";
  return f"Sua idade é {a}.Você é uma adolescente";

#variável que recebe a idade
idade = int(input("Informa a sua idade: "))

print(maior_idade(idade))