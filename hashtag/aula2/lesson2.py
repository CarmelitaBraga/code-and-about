import pandas as pd
# baixar numpy
# baixar openpyxl

table = pd.read_csv('/home/carmelita/Coding/Python/workshops/hashtag/aula2/telecom_users.csv')

# axis = 0 -> linha
# axis = 1 ->  coluna
# apaga a coluna inútil desejada
table = table.drop('Unnamed: 0', axis=1)
print(table)

# Converte todos os valores de uma coluna para numérico
# errors='ignore' or errors='raise' or errors='coerce'
table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors='coerce')

# excluir colunas em que todos os valores são vazios
# how='all' or how='any'
table = table.dropna(how='all', axis=1) # exclui valores vazios

# excluir linhas que possuem algum valor vazio
table = table.dropna(how='any', axis=0)


print(table.info())

















# Passo 3: Tratamento de dados
# resolver os valores que estão sendo reconhecidos de forma errada
# resolver valores vazios

# Passo 4: Análise inicial

# Passo 5: Análise detalhada 



"""import csv

with open('/home/carmelita/Coding/Python/workshops/hashtag/aula2/telecom_users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
"""
