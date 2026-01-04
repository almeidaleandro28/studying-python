import pandas as pd
import numpy as np
import random


# Seed for reproducibility
np.random.seed(42)

# Generate 100 rows of messy data
n_rows = 100

data = {
    'Transaction_ID': [1000 + i for i in range(n_rows)],
    'Date': [random.choice(['2023-05-01', '05/02/2023', '2023.05.03', '2023-05-04', np.nan]) for _ in range(n_rows)],
    'Customer_Name': [random.choice(['John DOE', 'john doe', ' Jane Smith', 'JANE SMITH ', 'Alice Brown', '  Alice brown', np.nan]) for _ in range(n_rows)],
    'Product_Category': [random.choice(['Electronics', 'electronics', 'HOME', 'Home ', '  Clothing', 'CLOTHING', '???']) for _ in range(n_rows)],
    'Price': [random.choice(['$100.00', '200.50', '300', 'not_set', '$150.75', np.nan]) for _ in range(n_rows)],
    'Quantity': np.random.randint(-5, 15, size=n_rows) # Includes negative numbers (errors)
}

df = pd.DataFrame(data)

# Inject 5 duplicate rows
duplicates = df.sample(n=5)
df = pd.concat([df, duplicates], ignore_index=True)

# Save to CSV
df.to_csv('practice_data.csv', index=False)