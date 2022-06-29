#-Mostre todos os filmes menos o “The Revenant”

#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')



#removendo os dados referentes ao filme The Revenant que está na ultima inha 88. Utilizando o metódo drop é 
#possível remover uma linha especifca
df.drop([88], inplace = True)

#imprimindo 
print(df)