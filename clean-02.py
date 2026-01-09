import pandas as pd
import numpy as np

data = pd.read_csv('practice_data.csv')

print('========== original============')
# print("info - \n", data.info() )
# print( "head - \n", data.head() )
# print("Missing value: \n", data.isnull().sum() )
# print("null var date \n", data.isnull())
print('========== cleaning=============')

# insert data with null - previous date
data['Date'] = pd.to_datetime( data[ 'Date' ], errors='coerce' )
data['Date'] = data['Date'].ffill()

# change value null for ohters
data['Customer_Name'] = data['Customer_Name'].fillna( 'others')
missingValueDate = data[ data[ 'Customer_Name' ].isnull() ]
data['Customer_Name'] = data['Customer_Name'].str.lower().str.strip()

# change $ of Price for space 
data['Price'] = data['Price'].str.strip().str.replace( "$", " ")
data['Price'] = data['Price'].str.strip().str.replace( "not_set", "000")
data['Price'] = data['Price'].astype(float)

groupyPriceQuant = data.groupby('Quantity')['Price'].transform( 'mean')
data['Price'] = data['Price'].fillna( groupyPriceQuant )
missingValuePrice = data[ data[ 'Price'].isnull() ]


data['Product_Category'] = data['Product_Category'].str.strip().str.lower()
data['Product_Category'] = data['Product_Category'].str.replace('???', 'olther_category')



# print("info - \n", data.info() )
# print( data.head() )
# print( data['Price'] == 0  )
print( missingValuePrice )
# print("Missing value: \n", data.isnull().sum()
