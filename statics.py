import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

region = data.groupby("Region")['Revenue'].sum()

product = data.groupby(["Product","Region" ])["Units Sold"].sum()
# product2= data.groupby(["Product"])["Units Sold"].sum().plot(kind='bar')
data.plot(x="Region", y="Revenue", kind="bar")
plt.show()
