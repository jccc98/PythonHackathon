import fredapi as fa
import pandas as pd
import plotly.express as px
## FRED API ##
fred = fa.Fred('6928edb718dc74993ad6d6387be1d1de ')

##TOTAL COMPENSATION ##

total_compensation_index = fred.get_series('ECIALLCIV')
total_compensation_info = fred.get_series_info('ECIALLCIV')


## INFLATION_INDEX ##
total_inflation_index = fred.get_series('CPIAUCSL')
total_inflation_info = fred.get_series_info('CPIAUCSL')
print(total_compensation_index.tail())
info = fred.get_series_info('CPIAUCSL')
print(info['title'])
df = pd.DataFrame()
df['consumer_price_all'] = fred.get_series('CPIAUCSL')
df.reset_index(inplace=True)
df.rename(columns = {'index':'date'})
print(df)
fig = px.line(df, x="index", y="consumer_price_all")
fig.show()