📊 Projeto de Análise de Dados com Python

Este projeto foi desenvolvido como parte do aprendizado no curso Fundamentos de Linguagem Python - Do Básico a Aplicações de IA,com o objetivo de aplicar na prática os conceitos estudados até o momento.

🧩 1. Problema de Negócio
Nossa loja de e-commerce está em fase de crescimento, registrando um volume cada vez maior de transações diárias. No entanto, essa grande quantidade de dados de vendas, em seu estado bruto, é como um baú de tesouro trancado: sabemos que há valor ali, mas não conseguimos acessá-lo.

Atualmente, muitas de nossas decisões estratégicas são baseadas em intuição e observações parciais, o que nos leva a enfrentar os seguintes desafios:

Gestão de Estoque Ineficiente: Não temos clareza sobre quais produtos são nossos “campeões de venda” e quais estão parados nas prateleiras. Isso resulta em excesso de estoque de itens de baixa procura e falta de produtos de alta demanda.

Marketing com Baixo Retorno: Nossas campanhas são genéricas, pois não sabemos quais categorias atraem mais clientes ou em quais regiões nosso público está concentrado.

Perda de Oportunidades Sazonais: Não conseguimos identificar padrões de vendas ao longo dos meses, o que impede o planejamento de promoções estratégicas e ações em períodos de baixa.

Expansão sem Direção: Temos o desejo de expandir, mas não sabemos quais mercados regionais são mais promissores.

O problema central é a falta de visibilidade clara sobre a performance do negócio, o que nos impede de tomar decisões rápidas, inteligentes e baseadas em evidências.

🎯 2. Objetivos do Projeto
Este projeto de análise de dados visa transformar nossos dados brutos de vendas em insights acionáveis.

O objetivo é responder a quatro perguntas de negócio fundamentais:

O que vender? → Identificar os produtos de maior sucesso para otimizar nosso portfólio e estoque.

Onde focar? → Compreender quais categorias de produtos geram a maior parte da receita.

Quando agir? → Analisar a performance de vendas ao longo do tempo para identificar tendências e sazonalidades.

Para onde expandir? → Mapear a distribuição geográfica de vendas para descobrir mercados mais fortes.

💡 3. Solução Proposta
A solução consiste em consolidar, limpar e analisar o histórico de dados de vendas da plataforma.

Com o uso de Python, Pandas, NumPy e Matplotlib, os dados são processados e transformados em visualizações claras e intuitivas para as equipes de gestão, marketing e operações.

🚀 4. Resultados Esperados e Benefícios de Negócio
Otimização de Estoque: Identificação dos produtos mais e menos vendidos para melhor controle de compras e estoque.

Marketing Direcionado e Eficaz: Criação de campanhas segmentadas por categoria e região, aumentando o ROI.

Planejamento Estratégico: Melhor gestão de recursos e previsibilidade financeira com base em tendências mensais

Decisões Baseadas em Dados: Desenvolvimento de uma cultura orientada por dados, substituindo a intuição por evidências concretas.

🧰 5. Tecnologias Utilizadas
Python 3.10+

Pandas – Manipulação e análise de dados (-v 2.2.3

NumPy – Operações matemáticas e numéricas (-v 1.26.4

Matplotlib / Seaborn – Visualização de dados (-v 3.9.2 / -v 0.13.2

Datetime / Timedelta – Manipulação de datas

Random – Geração de amostras aleatórias

⚙️ 6. Etapas do Processo
1️⃣ Geração de Dados Fictícios
Os dados foram criados dentro do próprio script, simulando um cenário real de e-commerce com:
- Produtos, categorias, preços
- Cidades, estados e clientes
- Datas de pedido e quantidades
- Atributos derivados como faturamento e status de entrega

2️⃣ Análise Exploratória Inicial
Incluiu a inspeção do dataset, medidas estatísticas e ajustes de tipos de dados.

3️⃣ Limpeza e Pré-Processamento
Conversão de colunas, criação de novos atributos e agrupamentos por período, categoria e região.

4️⃣ Análises e Visualizações
Foram respondidas perguntas de negócio com gráficos customizados:
- Top 10 produtos mais vendidos
- Evolução mensal do faturamento
- Faturamento por estado
- Faturamento por categoria
