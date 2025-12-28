import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id': [1,2,4,4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'City': ['NY', 'SF', None, 'NY']
})

# nullValue = df.isnull().sum()
# df.dropna()
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Age'] = df['Age'].fillna(000)
# df["City"] = df['City'].fillna('xxx')

# df['id'] = df['id'].astype(int)

# showDuplicate = df.duplicated()
# ------------------------------------------------

data2  = {
    'Transaction_ID': [101, 102, 102, 104, 105],
    'Customer_Name': [' alice smith', 'Bob Jones', 'Bob Jones', 'CHRIS redfield', '  jill valentine '],
    'Amount': ['$50.00', '$120.50', '$120.50', 'not_available', '$75.25'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023/01/04', np.nan]
}
df2 = pd.DataFrame( data2 )

print( "info datas:\n",df2.info() )
print('Data types:\n', df2.shape )
print("Missing value:\n", df2.isnull().sum())
print(df2)
print('------------ original -----------------')
print("----------- final check--------------")

df2['Customer_Name'] = df2['Customer_Name'].str.strip().str.title()
df2['Amount'] = df2['Amount'].replace('not_available', np.nan)
df2['Amount'] = df2['Amount'].str.replace('$', " ").astype(float)
df2['Date'] = pd.to_datetime( df2['Date'], dayfirst=True , format='mixed')

df2 = df2.drop_duplicates()

df2 = df2.dropna( subset=[ 'Date' ] )
df2['Amount'] = df2['Amount'].fillna( df2['Amount'].median() )


print('info datas: \n',df2.info())
print( df2 )