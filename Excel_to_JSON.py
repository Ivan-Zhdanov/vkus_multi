import pandas as pd
data = pd.read_excel("API_KEYS.xlsx", index_col=1)
print(data)
data.to_json('API_KEYS.json', orient='records')
