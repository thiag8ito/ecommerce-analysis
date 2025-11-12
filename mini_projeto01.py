import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

#Definição da função para gerar dados ficticios de vendas
def dsa_gera_dados_ficticios(num_registros = 600):
    """
    Gera um DataFrame do Pandas com dados e vendas ficticios
    """

    #Mensagem inicial indicando a quantidade de registros a serem gerados
    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    #Dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    #Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    #Dicionário com cidades e seus respctivos estados
    cidades_estados = {
         'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }
    
    #Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    #Lista que armazenará os registros de vendas
    dados_vendas = []

    #Define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    #Loop para gerar os registros de vendas
    for i in range(num_registros):

        #Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        #Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        #Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)

        #Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days= int(i/5), hours=random.randint(0, 23))

        #Se o produto for mouse ou teclado, aplica um desconto aleatorio de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        #Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

    #Mensagem final indicando que a geração terminou
    print("Geração de dados concluida\n")

    #Retorna os dados no formato de DataFrames
    return pd.DataFrame(dados_vendas)

#Gera os dados chamando a função da célula anterior
df_vendas = dsa_gera_dados_ficticios(500)

print(type(df_vendas))

print(df_vendas.shape)

print(f"\n{df_vendas.head()}")
print(f"\n{df_vendas.tail()}")
print(f"\n{df_vendas.info()}")
print(f"\n{df_vendas.describe()}")


#Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
#A coluna pode ser usada para análise temporal
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

#Engenharia de atributos
#Criando a coluna 'Faturamento' (preço x quantidade)
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

#Usando uma função lambda para criar uma coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

#Visualizando as informações do DF depois das alterações
print(df_vendas.info())

#Visualizando as informações dos pedidos depois das alterações
print(df_vendas.head())


"""Top 10 Produtos Mais Vendido"""
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

print(top_10_produtos)

#Define um estilo para os gráficos
sns.set_style('whitegrid')

#Cria  afigura e os eixos
plt.figure(figsize = (12, 7))

#Cria gráfico de barras horizontais
top_10_produtos.sort_values(ascending=True).plot(kind='barh', color='skyblue')

#Adicionar títulos e labels
plt.title('Top 10 produtos Mais Vendidos', fontsize=16)
plt.xlabel('Quantidade Vendida', fontsize=12)
plt.ylabel('Produto', fontsize=12)

#Exibe o gráfico
plt.tight_layout()
plt.show()


"""Faturamento Mensal"""
df_vendas['Mês'] = df_vendas['Data_Pedido'].dt.to_period('M')

#Agrupando por mês e soma o faturamento
faturamento_mensal = df_vendas.groupby('Mês')['Faturamento'].sum()
#Converte o indice para string para facilitar a plotagem no gráfico
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')
#Fortama para duas casas decimais
faturamento_mensal.map('R$ {:,.2f}'.format)

print(faturamento_mensal)

#Criando uma nova figura com tamanho de 12 por 6 polegadas
plt.figure(figsize=(12, 6))
#Plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind='line', marker='o', linestyle='-', color='green')
#Titulo do gráfico
plt.title('Evolução do Faturamento Mensal', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=.5)

plt.tight_layout()
plt.show()


"""Vendas Por Estado"""
vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)

#Formata para duas casas decimais
vendas_estado.map('R$ {:,.2f}'.format)

#Cria uma nova figura com tamanho de 12 por 7
plt.figure(figsize=(12, 7))

#Plota os dados de faturamento por estado em formato de gráfico de barras
vendas_estado.plot(kind='bar', color=sns.color_palette('husl', 7))

#Define o título do gráfico com fonte de tamanho 16
plt.title('Faturamento Por Estado', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Faturamento', fontsize=12)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


"""Faturamento por Categoria"""

faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

faturamento_categoria.map('R$ {:,.2f}'.format)

#Importa a função FuncFormatter para formatar os eixos
from matplotlib.ticker import FuncFormatter

faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

#Cria a Figura e os eixos (ax) com plt.subplots(), o que da mais controle sobre os elementos do gráfico
fig, ax = plt.subplots(figsize=(12, 7))

#Cria uma função para formatar os numeros
#Esta função recebe um valor 'y' e o transforma em uma string no formato 'R$ XX K'
def formatador_milhares(y, pos):
    return f'R$ {y/1000:,.0f}K'

#Cria o objeto formatador
formatter = FuncFormatter(formatador_milhares)

#Aplica o formatador ao eixo Y (ax.yaxis)
ax.yaxis.set_major_formatter(formatter)

faturamento_ordenado.plot(kind='bar', ax=ax, color=sns.color_palette('viridis', len(faturamento_ordenado)))

ax.set_title('Faturamento Por Categoria', fontsize=16)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_ylabel('Faturamento', fontsize=12)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()