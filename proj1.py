import pandas as pd

raw_data = pd.read_csv('./globalterrorismdb.csv', encoding='ISO-8859-1')
print(raw_data['scite1'][:7])