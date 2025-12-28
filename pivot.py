import pandas as pd

data = pd.read_csv( 'temp.csv' )

groupCity = data.groupby( [ 'Date','City' ] )['Temp'].sum()

pivotDate = data.pivot( index='Date', columns='City', values='Temp' )

pivotTableDFate = data.pivot_table(index='Date', columns='City', 
                                   values='Temp', aggfunc='sum')


example = {
    'Store': ['A', 'A', 'B', 'B'],
    'Sales': [100, 150, 200, 50],
    'Category': ['Food', 'Tech', 'Food', 'Tech']
}

# df = pd.DataFrame( example )

# groupSales = df.groupby('Store')['Sales'].sum()

example2 =  {
    'Date': ['Jan', 'Jan', 'Feb', 'Feb'],
    'Product': ['Apple', 'Orange', 'Apple', 'Orange'],
    'Sales': [100, 150, 120, 180],
    'Profit': [20, 35, 25, 45]
}

df2 = pd.DataFrame( example2 )

pivotDates = df2.pivot( index='Date', columns='Product', 
                       values=[ 'Sales', 'Profit' ] )
pivotDates2= df2.pivot_table( index='Date', columns='Product',
                              values=['Sales', 'Profit'])

# print( pivotDates )
# print( pivotDates2 )

# missing data
data3 = {
    'Region': ['North', 'North', 'South'],
    'Type': ['Retail', 'Online', 'Retail'],
    'Revenue': [500, 300, 400]
}
df3 = pd.DataFrame( data3 )

pivotRegion = df3.pivot_table( columns='Region', index='Type', 
                        values='Revenue', fill_value=0)

print( pivotRegion )