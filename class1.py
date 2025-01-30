import pandas as pd
import numpy as np

#Read Data
data = pd.read_json('Data/dados_hospedagem.json')
data = pd.json_normalize(data['info_moveis'])

#Transform Data
columns = list(data.columns)
data = data.explode(columns[3:]).reset_index(drop=True)

col_int = ['max_hospedes','quantidade_banheiros','quantidade_quartos','quantidade_camas'] 
data[col_int] = data[col_int].astype(np.int64)

col_to_clean = ['taxa_deposito','preco','taxa_limpeza']
data[col_to_clean] = data[col_to_clean].applymap(lambda x: float(x.replace('$', '').replace(',','').strip()))

col_float =['avaliacao_geral','taxa_deposito','preco','taxa_limpeza']
data[col_float] = data[col_float].astype(np.float64)

#Print Data
print(data.head())
print(data.info())