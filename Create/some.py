# need function
#need algorithm sort() DOES NOT COUNT use bubble sort ---> df.merge(df)
import pandas as pd

#sorting algorithm(bubble sort)
def bubble(A):
    n = len(A)
    i = 0
    for i in range(n - 1):

        j = 0
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:  
                A[j], A[j + 1] = A[j + 1], A[j] 
    return A
                
#reads data file / reomve empty space
with open('ad.dat', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

#links properties together
properties = [lines[i:i+7] for i in range(0, len(lines), 7)]

#makes data fram
df = pd.DataFrame(properties, columns=['Address', 'Street', 'Price', 
                                       'Bedrooms', 'Bathrooms', 'SquareFootage', 
                                       'LotSize'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df.to_string(index=False)

#converts from strings to numbers so sorting can happen
df['Price'] = pd.to_numeric(df['Price'])
df['Bedrooms'] = pd.to_numeric(df['Bedrooms'])
df['Bathrooms'] = pd.to_numeric(df['Bathrooms'])
df['SquareFootage'] = pd.to_numeric(df['SquareFootage'])
df['LotSize'] = pd.to_numeric(df['LotSize'])

# make variable to be able to sort prices with bubble sort
#prices = df['Price'].tolist()  # Convert the Price column to a list
#sorted_prices = bubble(prices)  # Sort the prices using bubble sort

#df_sorted = sorted_prices
#pandas black magic 
#df_sorted = df.sort_values(by='Price').reset_index(drop=True)

def bubble_sort_dataframe(df, column_name):
    n = len(df)
    for i in range(n):
        for j in range(0, n - i - 1):
            if df[column_name].iloc[j] > df[column_name].iloc[j + 1]:
                df.iloc[j], df.iloc[j + 1] = df.iloc[j + 1], df.iloc[j]
    return df
#bubble_sort_dataframe(df,'Price')
#print(df)
#while loop so user can go through all the options without the program closing 
while True:
    #menu and options
    x = int(input("1.) View all Properties  2.) Search based on Price  3.) EXIT "))
    
    if x == 1:
        print(df)
    elif x == 2:
        print("\nProperties sorted by Price:")
       
        bubble_sort_dataframe(df,'Price')
        print(df)
                       
        #print() #TODO need to print the sorted list
    elif x == 3:
        print("Exiting the program.")
        break  
    else:
        print("Invalid option. Please choose a valid option.")
