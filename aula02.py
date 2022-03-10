"""
Análise de dados com Python

Desafio:

Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes,
entre os principais estão internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu
que a empresa está com Churn (cancelamento de assinatura), de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs
"""

import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados para o Python

tabela = pd.read_csv(r'bd/telecom_users.csv')

# Passo 2: Visualizar a base de dados
# Entender as informações disponíveis
# Descobrir os problemas da base de dados
# axis = 0 -> Linha | axis = 1 -> coluna

tabela = tabela.drop('Unnamed: 0', axis=1)

# Passo 3: Tratamento de Dados
# analisar se o python está lendo as informações no formato correto

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# será que existe alguma coluna completamente vazia?

tabela = tabela.dropna(how='all', axis=1)

# será que existe algum campo vazio, sem informação, em alguma linha?

tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Passo 4: Análise inicial / Análise global
# quantos clientes cancelaram e quantos não cancelaram

print(tabela['Churn'].value_counts())

# % de clientes que cancelaram e que não cancelaram

print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5: Análise detalhada (buscar a causa / a solução dos cancelamentos)

# Criar os gráficos
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    # Exibir o gráfico
    grafico.show()

"""
Conclusões
- Clientes cancelam os planos com mais frequência nos primeiros meses
- Pessoas com famílias na mesma operadora, tem menos cancelamento
- Quanto mais serviços o cliente tem, menor o cancelamento
- Tem algum problema no serviço de fibra
- Contrato mensal tem mais cancelamento
- Taxa de cancelamento de pagamento por boleto é maior
"""
