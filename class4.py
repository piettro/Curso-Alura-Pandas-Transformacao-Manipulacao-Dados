import pandas as pd
import datetime

#Read Data
data = pd.read_json('Data/imoveis_disponiveis.json')

#Transform Date Data
data['data'] = pd.to_datetime(data['data'], format='%Y-%m-%d')
vagas_diponiveis_por_mes = data.groupby(data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum().reset_index()

#Print Data
print(vagas_diponiveis_por_mes.head())
print(data.head())
print(data.info())