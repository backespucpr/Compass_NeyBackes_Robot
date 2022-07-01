#Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x 
# em uma função e apresentar o resultado fora da função. Se o valor for impar, apresentar em 
# uma função a tabuada de 1 a 10 de X.

def parFatoral(num): 
    if num < 0: 
        return "Fatoral de números negativos não existe"
    elif num == 0: 
        return 1        
    else: 
        fat = 1        
        while(num > 1): 
            fat *= num          
            num -= 1
        return fat
#função que recebe o valor inserido e identifica se ele é par ou impar 
def imparPar(num):
    #caso o valor seja par ele é passado como paramêtro para verifcar o fatoral
    if (num % 2 == 0):
        return parFatoral(num)
    else:
        #caso o valor seja impar são impressos a tabuada de 1 a 10 referente ao valor impar digitado
        for value in range( 1, 11):
            print(f'{num} x {value} = {num * value}')
            

num = int(input('Informe o número:'));

print(imparPar(num))