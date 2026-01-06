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


# change $ of Price for space 
data['Price'] = data['Price'].str.strip().str.replace( "$", " ")
# print("info - \n", data.info() )

print( data)
# print("Missing value: \n", data.isnull().sum() )
