import pandas as pd

# Create a dataframe
df = pd.DataFrame()

# Add Hours column, starting trom zero, ending at 15 with step size of 5
df['Hours(n)'] = range(0,16,5)

# Calcualtion total number using hours
df['Total number'] = 200* 2**(df['Hours(n)'])

#show dataframe
print(df)

# show datafram in a better format
print(df)