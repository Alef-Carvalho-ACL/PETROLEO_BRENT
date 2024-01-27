# Previsão do Preço do Petróleo

## O Problema 📍

Este projeto foi desenvolvido para uma consultoria especializada na análise de dados do mercado de petróleo. O objetivo era criar uma ferramenta capaz de oferecer insights sobre a variação do preço do petróleo Brent e prever seu valor diário, considerando impactos de fatores como situações geopolíticas, crises econômicas e demanda global por energia.

## A Solução 🎯

Para resolver este problema, desenvolvemos um dashboard interativo e um modelo de Machine Learning para a previsão do preço do petróleo Brent. O modelo é capaz de capturar a dinâmica de séries temporais e considerar variáveis exógenas relevantes para a previsão.

### Etapas do Projeto ✅

1. **Análise Exploratória de Dados**: Iniciamos com uma análise exploratória para entender os padrões nos dados históricos do preço do petróleo.

2. **Modelagem de Previsão**: Aplicamos um modelo SARIMAX para capturar a natureza temporal dos dados e incluir informações exógenas no processo de previsão.

3. **Criação do Dashboard**: Utilizamos Streamlit e Power BI para criar um dashboard interativo que permite aos usuários visualizar dados históricos e realizar previsões de preço.

4. **Deploy do Modelo**: Preparamos um plano de deploy para colocar nossa solução em produção, garantindo que ela seja robusta, escalável e segura.

### Tecnologias Utilizadas 👨🏽‍💻

- Python
- Pandas e NumPy para manipulação de dados
- Statsmodels para modelagem estatística
- Streamlit para o dashboard interativo
- Joblib para salvar e carregar o modelo
- Git para controle de versão

### Instruções de Uso 📙

1. **Instalação**: Para usar o dashboard, é necessário ter Python instalado, bem como as bibliotecas listadas em `requirements.txt`.

2. **Execução**: Execute o dashboard localmente com o comando `streamlit run app.py` e siga as instruções na tela para visualizar os dados e fazer previsões.

### Deploy em Produção 🔎

Desenvolvemos um plano detalhado para o deploy do modelo em produção, considerando as melhores práticas de CI/CD, monitoramento e manutenção contínua.

---

Projeto desenvolvido por [Alef Carvalho].
