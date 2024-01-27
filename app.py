# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Carregar o modelo SARIMAX
model = joblib.load(r"C:\Users\alefc\OneDrive\Documentos\FIAP\Fase04\TechChall\model_sarimax_fitted.joblib")

# Streamlit
st.markdown("<h1 style='text-align: center; '> Previsão do Preço do Petróleo 🤑</h1>", unsafe_allow_html=True)
st.warning('Preencha o formulário com o valor do petróleo e a quantidade de dias (máximo 10 dias) e clique no botão **ENVIAR** no final da página para efetuarmos uma projeção.')

# Entrada do Preço Atual do Petróleo
current_price = st.number_input('Insira o valor atual do petróleo:', format='%f')

# Entrada para Número de Dias de Previsão (limitado a 10 dias)
prediction_days = st.number_input('Quantos dias à frente deseja prever? (limitado a 10 dias)', min_value=1, max_value=10)

if st.button('Fazer Previsão'):
    if current_price > 0 and prediction_days > 0:
        try:
            # Criar um DataFrame com os dados de entrada
            exog_data = pd.DataFrame({
                '7_day_MA': np.full((prediction_days,), current_price),
                '7_day_volatility': np.zeros((prediction_days,))
            })

            # Fazer a previsão com o modelo SARIMAX
            forecast_results = model.get_forecast(steps=prediction_days, exog=exog_data)
            forecast_values = forecast_results.predicted_mean

            # Formatar os valores previstos para o formato monetário
            forecast_values_formatted = forecast_values.apply(lambda x: f'USD {x:.2f}')

            # Criar um DataFrame para os valores previstos formatados
            forecast_df = pd.DataFrame({
                'Data': pd.date_range(start=pd.to_datetime('today'), periods=prediction_days, freq='D'),
                'Previsão (USD)': forecast_values_formatted.values
            })

            # Exibir os resultados formatados com um título claro e o nome do campo
            st.write(f'Previsão para os próximos {prediction_days} dias:')
            st.table(forecast_df.set_index('Data'))
        except Exception as e:
            st.error(f'Ocorreu um erro: {e}')
    else:
        st.error('Por favor, insira valores válidos.')