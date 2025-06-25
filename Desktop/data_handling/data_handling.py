import pandas as pd

# Read file
df = pd.read_csv('customers.csv')

# Fill missing ages with mean
df['age'].fillna(df['age'].mean(), inplace=True)

# Insert new record
new_row = {'id': 4, 'name': 'David', 'age': 22, 'city': 'Chicago'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Update Bob's city
df.loc[df['id']==2, 'city'] = 'San Francisco'

# Delete Alice's record
df = df[df['id'] != 1]

# Save cleaned file
df.to_csv('customers_cleaned.csv', index=False)
print('✅ Done! Clean file saved as customers_cleaned.csv')
