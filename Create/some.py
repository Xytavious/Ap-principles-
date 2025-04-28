# Rental Property Manager or Inventory Manager
# rental properties, tenants, and rent due
# stock levels, sales, and reorders
# need 2 functions 
#make table with surch alg to pull data 
# make options to add data /
import pandas as pd

with open('ad.dat', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]  # remove empty lines

properties = [lines[i:i+7] for i in range(0, len(lines), 7)]

df = pd.DataFrame(properties, columns=['Address', 'Street', 'Price', 'Bedrooms', 'Bathrooms', 'SquareFootage', 'LotSize'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df.to_string(index=False))

df['Price'] = pd.to_numeric(df['Price'])
df['Bedrooms'] = pd.to_numeric(df['Bedrooms'])
df['Bathrooms'] = pd.to_numeric(df['Bathrooms'])
df['SquareFootage'] = pd.to_numeric(df['SquareFootage'])
df['LotSize'] = pd.to_numeric(df['LotSize'])
df_sorted = df.sort_values(by='Price')

with open('sorted_ad.dat', 'w') as f:
    for _, row in df_sorted.iterrows():
        f.write(f"{row['Address']}\n{row['Street']}\n{row['Price']}\n{row['Bedrooms']}\n{row['Bathrooms']}\n{row['SquareFootage']}\n{row['LotSize']}\n")
    while True:
        # Display the menu
        x = int(input("1.) View all Properties  2.) Search based on Price  3.) EXIT "))

        # Handle user input for each option
        if x == 1:
            print(df)
        elif x == 2:
            print(df_sorted)
        elif x == 3:
            print("Exiting the program.")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please choose a valid option.")