import fredapi as fa
import pandas as pd
import plotly.express as px
import pandas_datareader as pdr
## FRED API ##
fred = fa.Fred('6928edb718dc74993ad6d6387be1d1de ')

###DATA FRAME FUNCTION ##
def get_fred_data(param_list, start_date, end_date):
  df = pdr.DataReader(param_list, 'fred', start_date, end_date)
  return df.reset_index()

##TOTAL COMPENSATION ##

total_compensation_info = fred.get_series_info('ECIALLCIV')
#print(total_compensation_info['title'])
series ='ECIALLCIV'
compensation_df = get_fred_data(param_list=[series], start_date= '2012-01-01', end_date='2030-01-01')
compensation_df.rename(columns = {'ECIALLCIV':'Total compensation'}, inplace = True)


## INFLATION_INDEX ##
info = fred.get_series_info('CPIAUCSL')
#print(info['title'])
series = 'CPIAUCSL'
inflation_df = get_fred_data(param_list=[series], start_date= '2012-01-01', end_date='2030-01-01')
inflation_df.rename(columns = {'CPIAUCSL':'All Items in U.S. City Average'}, inplace = True)

### Corelation - Compensation and inflation ##
df_compensation_and_inflation = pd.concat([compensation_df, inflation_df])
#print(df_compensation_and_inflation)
fig = px.line(df_compensation_and_inflation, x="DATE", y=["All Items in U.S. City Average", "Total compensation"])
#fig.show()

###Iron and steel cost ###
steel_cost_index = fred.get_series_info('WPU101')
series = 'WPU101'
iron_and_steel_df = get_fred_data(param_list=[series], start_date= '2012-01-01', end_date='2030-01-01')
iron_and_steel_df.rename(columns = {'WPU101':'Iron and Steel cost'}, inplace = True)
#print(steel_cost_index['title'])
#print(steel_cost_index)


###Global price of Aluminum###
aluminum_cost_info = fred.get_series_info('PALUMUSDM')
series = 'PALUMUSDM'
aluminum_cost_df = get_fred_data(param_list=[series], start_date='2012-01-01', end_date ='2030-01-01')
aluminum_cost_df.rename(columns= {'PALUMUSDM': 'aluminum cost'}, inplace = True)
print(aluminum_cost_df)


#Glass and Glass Product Manufacturing Cost##
glass_cost_info = fred.get_series_info('PCU3272132721')
series = 'PCU3272132721'
glass_cost_df = get_fred_data(param_list=[series],  start_date='2012-01-01', end_date ='2030-01-01')
glass_cost_df.rename(colums= {'PCU3272132721': 'glass cost'}, inplace = True)

##Plastic and Rubber Products Manufacturing Cost##
plastic_and_rubber_info = fred.get_series_info('COINDUSZ326')
series = 'COINDUSZ326'
plastic_and_rubber_cost_df = get_fred_data(param_list=[series],  start_date='2012-01-01', end_date ='2030-01-01')
plastic_and_rubber_cost_df.rename(columns= {'COINDUSZ326': 'plastic and rubber cost'}, inplace = True)