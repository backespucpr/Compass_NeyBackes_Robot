#-3- Crie mais uma coluna em tempo de execução juntando os dadosmovie e year

#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#imprimindo valores entre 1987 a 1999 que estão nas linhas 59 a 71
print(df[59:72])
