#  Análise de Oportunidades no Mercado Imobiliário Brasileiro

##  Descrição do Projeto

Este projeto tem como objetivo analisar a relação entre a **quantidade de consumidores** na faixa etária de **38 a 58 anos** e o **número de empresas de construção civil ativas** em cada estado do Brasil. O foco é identificar **mercados saturados** e **oportunidades futuras de investimento** no setor imobiliário.

Para isso, foram utilizadas técnicas de **processamento de dados, modelagem estatística e aprendizado de máquina não supervisionado** para prever tendências e realizar agrupamentos baseados na razão **Consumidores/Empresas**.

---

##  Objetivos

- **Determinar Estados Saturados** → Mercados onde a concorrência é alta e o crescimento pode ser limitado.
- **Identificar Oportunidades** → Estados com **poucas empresas por consumidor**, indicando potencial para novas incorporações imobiliárias.
- **Analisar Tendências (2007-2022)** → Utilizar dados históricos e projeções para entender a evolução do mercado ao longo do tempo.
- **Agrupar Estados Semelhantes** → Aplicar **técnicas de clustering** (K-Means) para segmentar os estados de acordo com o comportamento do mercado imobiliário.

---

## 🛠 Tecnologias Utilizadas

O projeto utiliza as seguintes ferramentas e bibliotecas:

-  **Python**
-  **Pandas, NumPy, SciPy** (Manipulação e análise de dados)
-  **Matplotlib, Seaborn, Plotly** (Visualização de dados)
-  **Scikit-learn** (Machine Learning – K-Means Clustering)
-  **GeoPandas** (Mapeamento geográfico)
-  **API do IBGE (SIDRA)** (Coleta de dados populacionais e empresariais)

---

## 📂 Estrutura do Projeto

```
RealEstateMarketAnalysisBrazil/
│
├── requirements.txt        # Lista de dependências do projeto
├── setup_environment.py    # Script Python para configuração do ambiente automatico (windows)
├── notebook.ipynb          # Notebook Jupyter com toda a análise e visualizações
├── data/                   # Pasta com arquivos CSV processados
│   ├── combined_population_to_companies.csv
│   ├── extrapolated_population_companies_separate_methods.csv
│   ├── state_clusters.csv
|   ├── ...
│   └── correlation_by_state.csv
├── charts_ratio/           # Gráficos gerados na extrapolação dos dados
├── README.md               # Este arquivo de documentação
└── relatorio.pdf           # Relatório final da análise
```

---

##  Como Executar o Projeto

###  Criar um Ambiente Virtual
No terminal, execute:

```bash
python -m venv env
```

Ative o ambiente:
- **Windows**:  
  ```bash
  .\env\Scripts\activate
  ```
- **Linux/Mac**:  
  ```bash
  source env/bin/activate
  ```

###  Instalar as Dependências 
```bash
pip install -r requirements.txt
```
 Ou no próprio arquivo notebook (.ipynb). Existe uma célula responsavel por isso após abrir o notebook. 


###  Executar o Jupyter Lab
```bash
jupyter-lab
```

Abra o arquivo `notebook.ipynb` e selecione o kernel **Python (env)**.


Após isso, execute cada uma das células do notebook. Os dados vão ser processados, os gráficos serão gerados, à medida que as células executarem.

---

##  Metodologia

1️ **Coleta de Dados**  
   - População por faixa etária (38-58 anos) via **IBGE (SIDRA)**  
   - Número de empresas ativas via **Tabela 1757 do SIDRA**  

2️ **Processamento dos Dados**  
   - Cálculo da **Razão Consumidores/Empresas**  
   - Interpolação e extrapolação para **2021 e 2022**  

3️ **Análise e Agrupamento dos Estados**  
   - Clusterização dos estados via **K-Means**  
   - Classificação:
     - ** Saturado (Muitas empresas para poucos consumidores)**
     - ** Estável (Mercado equilibrado)**
     - ** Oportunidade (Poucas empresas para muitos consumidores)**

4️ **Visualizações e Relatório**  
   - Mapas interativos  
   - Gráficos de evolução temporal  
   - Relatório detalhado com insights estratégicos  

---

Os estados foram segmentados em três categorias:

| Cluster | Categoria       | Característica |
|---------|---------------|---------------|
| 2       | Oportunidade  | Maior demanda do que oferta, ideal para expansão. |
| 1       | Estável       | Mercado equilibrado entre empresas e população. |
| 0       | Saturado      |  Alta concorrência e menor margem para novos negócios. |

🔗 **[📄 Clique aqui para acessar o relatório completo](Document.pdf)**

---

## 📌 Autor

**Mantenedor**: [Micael Balza]  
🔗 [LinkedIn](https://www.linkedin.com/in/micael-balza/) | 📧 [Email](mailto:micaelbalza@hotmail.com)

---

## 📄 Licença

Este projeto está sob a **Licença MIT**. Você pode usá-lo e modificá-lo livremente.

---

📌 **Caso tenha dúvidas ou sugestões, entre em contato! 🚀**



