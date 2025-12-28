import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

region = data.groupby("Region")['Revenue'].sum()

product = data.groupby(["Region" ])["Units Sold"].sum()
# product2= data.groupby(["Product"])["Units Sold"].sum().plot(kind='bar')
productMult = data.groupby('Product').agg( {'Revenue': ['sum', 'mean']})

# data.plot(x="Region", y="Revenue", kind="bar")
# plt.show()

# product.plot( kind="bar", title="title")
# plt.ylabel("Revenue")
# plt.show()

# productMult.plot( kind='bar',  title='title')
# # plt.ylabel('Region')
# plt.show()

# revenue more 100
# revenueMore100 = data.groupby('Product').apply( lambda g: g[g['Revenue'] > 100 ]
#                                                , include_groups=False)
# print( revenueMore100)

soldMore10 = data.groupby('Revenue').apply( lambda g: g +  100)