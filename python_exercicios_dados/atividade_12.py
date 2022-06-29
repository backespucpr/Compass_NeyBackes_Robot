#-Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.


#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#da mesma forma que foi feito na atividade anterior esta resposta está na coluna Name na linha 63 e 88
vencedor2016 = df['Name'][63]
vencedor1991 = df['Name'][88]
#imprimindo nossa resposta
print(f'''Nome do ator que ganhou o Oscar em 1993 \n
O vencedor de 1991 foi {vencedor2016}
O vencedor de 2016 foi {vencedor1991}
''')

