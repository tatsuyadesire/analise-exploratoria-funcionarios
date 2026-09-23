# Análise Exploratória de Dados de Funcionários

## 1. Sobre o projeto

Este projeto foi desenvolvido para a disciplina de **Análise Exploratória de Dados**, com o objetivo de aplicar técnicas de análise e visualização de dados para identificar padrões, distribuições, relações e possíveis discrepâncias em um conjunto de dados organizacionais.

O projeto utiliza dados fictícios de funcionários de uma organização, considerando informações relacionadas a idade, departamento, cargo, experiência profissional, jornada de trabalho, trabalho remoto, desempenho, salário e satisfação.

Além das análises realizadas em notebooks, foi desenvolvido um **dashboard interativo em Streamlit**, permitindo explorar os dados de maneira visual e dinâmica.

---

## 2. Objetivos

Os principais objetivos do projeto são:

- Explorar um conjunto de dados organizacionais;
- Identificar a distribuição das principais variáveis;
- Analisar características dos funcionários;
- Comparar informações entre departamentos;
- Identificar possíveis valores discrepantes;
- Investigar relações entre salário, satisfação e horas trabalhadas;
- Utilizar gráficos para facilitar a interpretação dos dados;
- Desenvolver um dashboard interativo para exploração dos resultados.

---

## 3. Tecnologias utilizadas

O projeto foi desenvolvido utilizando Python e as seguintes bibliotecas:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

---

## 4. Estrutura do projeto

    Visualização de dados/
    │
    ├── data/
    │   └── funcionarios.csv
    │
    ├── dashboards/
    │   └── dashboard.py
    │
    ├── notebooks/
    │   └── análises realizadas durante o projeto
    │
    └── README.md

---

# 5. Dataset

O conjunto de dados possui informações referentes a 20 funcionários.

As variáveis originais são:

| Variável | Descrição |
|---|---|
| ID | Identificador do funcionário |
| Nome | Nome do funcionário |
| Idade | Idade do funcionário |
| Departamento | Departamento ao qual pertence |
| Cargo | Cargo ocupado |
| Experiência (anos) | Tempo de experiência profissional |
| Horas Semanais | Quantidade de horas semanais |
| Remoto | Indica se o funcionário trabalha remotamente |
| Desempenho | Indicador de desempenho |

Para atender às análises propostas na atividade, também foram utilizadas as variáveis:

| Variável | Descrição |
|---|---|
| Salário | Salário utilizado na análise |
| Satisfação | Nível de satisfação utilizado na análise |
| Horas Trabalhadas | Quantidade de horas trabalhadas |

As variáveis de **salário** e **satisfação** foram simuladas para possibilitar as análises solicitadas na atividade.

---

# 6. Carregamento e preparação dos dados

Inicialmente, o arquivo CSV foi carregado utilizando Pandas.

    import pandas as pd

    df = pd.read_csv("../data/funcionarios.csv")

Após o carregamento, foram realizadas verificações iniciais para compreender a estrutura do dataset.

    df.head()

    df.info()

    df.describe()

Também foram verificadas informações relacionadas a valores ausentes e registros duplicados.

    df.isnull().sum()

    df.duplicated().sum()

A análise inicial permitiu verificar a estrutura das variáveis e preparar os dados para a etapa de visualização.

---

# 7. Análise exploratória

## 7.1 Distribuição das idades

A primeira análise realizada foi referente à distribuição das idades dos funcionários.

Foi utilizado um histograma para visualizar a frequência dos diferentes grupos de idade.

A idade dos funcionários apresenta uma distribuição concentrada principalmente entre adultos jovens e adultos de meia-idade.

Os valores observados estão aproximadamente entre **24 e 46 anos**, com maior concentração na faixa dos **20 aos 30 anos**.

A visualização permite perceber que não existe uma concentração extrema em apenas uma idade específica, mas há maior presença de funcionários mais jovens no conjunto analisado.

### Interpretação

A distribuição indica uma equipe composta predominantemente por funcionários jovens e adultos, com alguns funcionários apresentando idades mais elevadas.

Essa característica pode estar relacionada à própria composição fictícia utilizada no dataset e não deve ser generalizada para uma população real.

---

# 8. Distribuição salarial

A distribuição dos salários foi analisada por meio de gráficos de distribuição e comparações entre departamentos.

Os valores simulados apresentam diferenças consideráveis entre os funcionários.

A maior concentração está aproximadamente na faixa de **R$ 4.000 a R$ 8.000**, enquanto alguns funcionários apresentam salários superiores a essa faixa.

Também existem salários mais baixos associados principalmente a cargos de entrada, como estágio e assistência.

### Interpretação

A diferença salarial está relacionada principalmente às características dos cargos e departamentos.

Funcionários em cargos de maior responsabilidade apresentam salários mais elevados, enquanto cargos de entrada apresentam valores menores.

---

# 9. Salário por departamento

Para analisar diferenças entre departamentos, foi calculada a média salarial de cada área.

O gráfico permite comparar diretamente os níveis salariais entre os departamentos.

De forma geral, os departamentos de **TI e Finanças** apresentam concentrações de salários mais elevados, enquanto áreas como **Vendas, RH e Marketing** apresentam valores mais distribuídos.

Essa diferença também está relacionada aos cargos existentes dentro de cada departamento.

### Interpretação

Não é possível atribuir a diferença salarial exclusivamente ao departamento.

O cargo e o nível de experiência também possuem influência importante sobre os salários observados.

Por esse motivo, a comparação por departamento deve ser interpretada juntamente com as informações de cargo e experiência.

---

# 10. Distribuição salarial por departamento utilizando Boxplot

Foi utilizado um boxplot para analisar a distribuição salarial de cada departamento.

O boxplot permite observar:

- Mediana;
- Quartis;
- Dispersão;
- Valores mínimos e máximos;
- Possíveis valores discrepantes.

A utilização do boxplot facilita a comparação entre os departamentos porque permite observar não apenas a média, mas também a distribuição dos salários.

### Interpretação

Alguns departamentos apresentam maior dispersão salarial.

Essa dispersão ocorre porque diferentes cargos e níveis de experiência estão presentes dentro de uma mesma área.

Valores mais elevados não devem ser automaticamente considerados erros ou anomalias.

Eles podem representar funcionários com cargos de maior responsabilidade ou maior experiência.

---

# 11. Análise de valores discrepantes

Os boxplots também foram utilizados para identificar possíveis outliers.

Um valor discrepante é uma observação que se encontra distante da maior parte dos dados.

Entretanto, um valor discrepante estatisticamente não significa necessariamente que exista um erro no dataset.

No contexto organizacional, um salário elevado, por exemplo, pode ser perfeitamente justificável caso esteja associado a um cargo de gestão ou alta especialização.

Portanto, os possíveis outliers devem ser interpretados considerando o contexto das demais variáveis.

---

# 12. Distribuição da satisfação

A variável de satisfação foi analisada utilizando gráficos de distribuição.

Os valores simulados apresentam níveis de satisfação relativamente próximos, concentrados aproximadamente entre **7 e 8,5**.

Isso indica que não existe uma grande dispersão entre os níveis de satisfação observados.

### Interpretação

A maior parte dos funcionários apresenta níveis de satisfação relativamente elevados dentro da escala utilizada.

Porém, como os dados de satisfação foram simulados para fins acadêmicos, esses valores não representam uma pesquisa real de satisfação organizacional.

---

# 13. Distribuição das horas trabalhadas

A quantidade de horas trabalhadas foi analisada por meio de gráficos de distribuição.

A maior parte dos funcionários apresenta jornadas próximas de **40 horas semanais**, enquanto alguns funcionários apresentam jornadas inferiores ou superiores.

Existem funcionários com jornadas próximas de 30 horas e outros próximos de 50 horas.

### Interpretação

A maior concentração próxima de 40 horas indica uma jornada predominante semelhante entre os funcionários.

As diferenças observadas podem estar relacionadas aos cargos e às características das funções desempenhadas.

---

# 14. Análise de desempenho

O desempenho dos funcionários também foi considerado na análise exploratória.

Os valores apresentam diferenças entre os funcionários e permitem observar que o desempenho não é uniforme dentro da organização.

Funcionários pertencentes a diferentes departamentos e cargos apresentam diferentes níveis de desempenho.

### Interpretação

O desempenho deve ser analisado juntamente com outras variáveis.

Não é adequado concluir que salário, experiência ou quantidade de horas trabalhadas, isoladamente, determinam o desempenho de um funcionário.

---

# 15. Relação entre salário e satisfação

Foi elaborado um gráfico de dispersão relacionando:

**Salário × Satisfação**

Cada ponto representa um funcionário.

O objetivo dessa visualização é verificar se existe uma relação linear perceptível entre o salário recebido e o nível de satisfação.

A análise visual não apresenta uma relação linear forte entre as duas variáveis.

Funcionários com salários mais elevados não necessariamente apresentam os maiores níveis de satisfação.

Da mesma forma, funcionários com salários menores não necessariamente apresentam baixa satisfação.

### Interpretação

Dentro do conjunto analisado, não existe evidência visual suficiente para afirmar que o aumento do salário está diretamente associado ao aumento da satisfação.

A satisfação pode estar relacionada a diversos outros fatores, como:

- Cargo;
- Ambiente de trabalho;
- Jornada;
- Relação com colegas;
- Responsabilidades;
- Experiência;
- Condições de trabalho;
- Trabalho remoto.

Portanto, salário e satisfação não apresentam uma relação simples no conjunto analisado.

---

# 16. Relação entre horas trabalhadas e salário

Também foi criado um gráfico de dispersão relacionando:

**Horas Trabalhadas × Salário**

Essa visualização permite observar se funcionários que trabalham mais horas também apresentam salários maiores.

O gráfico apresenta uma tendência de aumento dos salários em alguns funcionários com jornadas maiores.

Entretanto, essa relação não deve ser interpretada como uma relação de causa e efeito.

### Interpretação

Funcionários que trabalham mais horas podem também ocupar cargos que naturalmente possuem salários maiores.

Por exemplo, cargos de maior responsabilidade podem apresentar simultaneamente:

- Maior salário;
- Maior experiência;
- Maior quantidade de horas trabalhadas.

Assim, a relação observada pode estar associada às características dos cargos e não necessariamente ao número de horas trabalhadas isoladamente.

---

# 17. Respostas às questões propostas

## 17.1 Como é a distribuição das idades dos funcionários?

As idades estão distribuídas aproximadamente entre **24 e 46 anos**, com maior concentração entre funcionários mais jovens, especialmente na faixa dos 20 aos 30 anos.

Não existe uma única idade dominante, mas existe uma concentração maior nessa faixa.

---

## 17.2 Há setores com maior concentração de salários altos?

Sim.

Os departamentos de **TI e Finanças** apresentam maior concentração de salários elevados no conjunto analisado.

Entretanto, essa diferença também está relacionada aos cargos e aos níveis de experiência existentes em cada departamento.

---

## 17.3 Existe uma relação perceptível entre o salário e o nível de satisfação?

Não foi identificada uma relação linear forte entre salário e satisfação.

Funcionários com salários elevados não necessariamente apresentam maior satisfação.

Portanto, dentro do conjunto analisado, o salário isoladamente não explica os níveis de satisfação observados.

---

## 17.4 Funcionários que trabalham mais horas apresentam maior insatisfação?

Não.

A análise não apresenta uma relação clara que permita afirmar que funcionários que trabalham mais horas são necessariamente mais insatisfeitos.

A satisfação apresenta variações independentes da quantidade de horas trabalhadas.

---

# 18. Dashboard interativo

Além das análises realizadas nos notebooks, foi desenvolvido um dashboard interativo utilizando **Streamlit** e **Plotly**.

O dashboard foi desenvolvido para permitir uma exploração visual dos dados de maneira mais dinâmica.

O título principal utilizado é:

**ANÁLISE DE FUNCIONÁRIOS**

---

# 19. Indicadores principais

O dashboard apresenta cinco indicadores principais:

| Indicador | Descrição |
|---|---|
| Funcionários | Quantidade de funcionários presentes no filtro atual |
| Salário médio | Média salarial dos funcionários filtrados |
| Satisfação média | Média da satisfação dos funcionários filtrados |
| Horas médias | Média das horas trabalhadas |
| Desempenho médio | Média do desempenho |

Os indicadores são atualizados de acordo com os filtros selecionados.

---

# 20. Gráficos do dashboard

O dashboard possui cinco visualizações principais.

## 20.1 Salário médio por departamento

Apresenta a média salarial de cada departamento.

Permite comparar os níveis salariais entre as diferentes áreas da organização.

---

## 20.2 Satisfação média por departamento

Apresenta a satisfação média dos funcionários agrupados por departamento.

Esse gráfico permite observar diferenças nos níveis médios de satisfação entre as áreas.

---

## 20.3 Distribuição salarial por departamento

Utiliza boxplots para apresentar a distribuição dos salários dentro de cada departamento.

O gráfico permite observar:

- Mediana;
- Quartis;
- Dispersão;
- Valores extremos;
- Diferenças entre departamentos.

---

## 20.4 Salário × Satisfação

Apresenta um gráfico de dispersão relacionando salário e satisfação.

Cada ponto representa um funcionário.

O objetivo é permitir a identificação visual de possíveis relações entre essas variáveis.

---

## 20.5 Horas Trabalhadas × Salário

Apresenta a relação entre quantidade de horas trabalhadas e salário.

A visualização permite observar possíveis tendências e agrupamentos entre as duas variáveis.

---

# 21. Filtros do dashboard

O dashboard possui filtros interativos para facilitar a exploração dos dados.

Os filtros disponíveis são:

- Departamento;
- Cargo;
- Faixa etária;
- Faixa salarial;
- Experiência;
- Satisfação;
- Horas trabalhadas.

Ao modificar os filtros, os indicadores e gráficos são atualizados de acordo com o subconjunto selecionado.

---

# 22. Interatividade

As visualizações foram desenvolvidas utilizando Plotly.

Isso permite interações como:

- Passar o mouse sobre os elementos;
- Visualizar valores;
- Aplicar zoom;
- Explorar pontos específicos;
- Redimensionar as visualizações.

As ferramentas adicionais dos gráficos são exibidas de maneira discreta, aparecendo quando o usuário interage com a visualização.

---

# 23. Diferença entre notebook e dashboard

O projeto possui duas abordagens complementares.

### Notebook

Os notebooks foram utilizados para:

- Carregamento dos dados;
- Exploração inicial;
- Tratamento e preparação;
- Estatísticas descritivas;
- Construção dos gráficos;
- Análise dos resultados;
- Interpretação dos padrões encontrados.

### Dashboard

O dashboard foi desenvolvido para:

- Facilitar a exploração dos resultados;
- Permitir aplicação de filtros;
- Apresentar indicadores de forma resumida;
- Facilitar comparações;
- Permitir uma análise mais interativa.

Dessa forma, o notebook concentra a parte analítica e o dashboard concentra a exploração visual e interativa.

---

# 24. Principais padrões identificados

A análise exploratória permitiu identificar alguns padrões no conjunto de dados.

### Idade

A maior parte dos funcionários está concentrada em faixas de idade mais jovens, embora exista uma variação considerável entre os indivíduos.

### Salário

Existe uma diferença salarial significativa entre os funcionários.

Os maiores salários estão concentrados principalmente em determinados departamentos e cargos.

### Satisfação

Os níveis de satisfação apresentam uma variação relativamente pequena no conjunto analisado.

### Horas trabalhadas

A jornada está concentrada principalmente próxima de 40 horas semanais, com algumas observações acima e abaixo desse valor.

### Salário e satisfação

Não foi observada uma relação linear forte entre salário e satisfação.

### Horas trabalhadas e salário

Existe uma tendência de salários maiores em alguns funcionários com jornadas maiores, mas essa relação também pode estar associada ao cargo e à experiência.

---

# 25. Conclusões

A análise exploratória demonstrou como técnicas de visualização podem facilitar a compreensão de um conjunto de dados organizacionais.

Os histogramas permitiram compreender a distribuição das variáveis numéricas, enquanto os boxplots possibilitaram comparar distribuições e identificar possíveis valores discrepantes.

Os gráficos de dispersão permitiram analisar relações entre variáveis e verificar que algumas associações não são necessariamente lineares.

Entre os principais resultados observados estão:

- Maior concentração de funcionários em faixas etárias mais jovens;
- Diferenças salariais entre os departamentos;
- Maior concentração de salários elevados em TI e Finanças;
- Distribuição de satisfação relativamente concentrada;
- Predominância de jornadas próximas de 40 horas;
- Ausência de uma relação linear forte entre salário e satisfação;
- Ausência de evidência clara de que jornadas maiores resultem necessariamente em menor satisfação;
- Existência de possíveis relações entre salário, horas trabalhadas, cargo e experiência.

A análise também demonstra a importância de evitar conclusões baseadas em uma única variável.

Uma diferença salarial entre departamentos, por exemplo, pode estar relacionada não apenas ao departamento, mas também aos cargos e à experiência dos funcionários.

Da mesma forma, uma associação entre horas trabalhadas e salário não significa necessariamente que uma variável seja responsável pela outra.

---

# 26. Limitações

O dataset utilizado possui apenas 20 funcionários e representa um conjunto de dados fictício para fins acadêmicos.

Além disso, as variáveis de salário e satisfação foram simuladas para permitir a realização das análises solicitadas na atividade.

Por esse motivo, os resultados não devem ser interpretados como representativos de uma organização real.

As conclusões apresentadas são válidas apenas para o conjunto de dados analisado.

---

# 27. Como executar o projeto

Primeiramente, é necessário instalar as dependências.

    pip install -r requirements.txt

Para executar o dashboard:

    streamlit run dashboards/dashboard.py

Após executar o comando, o Streamlit disponibilizará o dashboard no navegador.

---

# 28. Requirements

As principais dependências utilizadas no projeto são:

    pandas==3.0.6
    numpy==2.5.3
    matplotlib==3.11.2
    seaborn==0.13.2
    jupyter==1.1.1
    notebook==7.6.2
    ipykernel==7.3.0
    streamlit==1.64.0
    plotly==7.1.0

---

# 29. Resultado final

O projeto combina análise exploratória, estatística descritiva e visualização de dados em Python.

A utilização dos notebooks permite documentar o processo de análise, enquanto o dashboard oferece uma interface interativa para exploração dos resultados.

Dessa forma, o projeto demonstra na prática como a visualização de dados pode ser utilizada como ferramenta de apoio à análise exploratória, permitindo identificar distribuições, diferenças, padrões, tendências e possíveis relações entre variáveis.