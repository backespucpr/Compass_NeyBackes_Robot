#Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, 
#meses e dias. Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e 
#todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses 
#e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar 
#raciocínio matemático simples.



def calculoIdade(idadeDias):

    ano = idadeDias // 365
    mes = (idadeDias % 365) // 30
    dias = (idadeDias % 365) % 30    
    return f'''
    Ano: {ano}
    Meses: {mes}
    dias: {dias}'''

idadeDias = int(input('Informe a idade em dias '));


print(calculoIdade(idadeDias))




