# need function
#need algorithm sort() DOES NOT COUNT use bubble sort ---> df.merge(df)
import pandas as pd
class mergesort:
    @staticmethod
    def sort(a):
        if len(a) > 1:
            mid = len(a)/2
            l = a[:mid]
            r = a[mid:]
            mergesort(l)
            mergesort(r)
            mergesort(a,l,r)

    @staticmethod
    def Merge(A,L,R):
        i = 0
        j =0
        k=0
       
        while i < len(L) and j < len(R):
            if L[i] < [j]:
                A[k] = L[i]
                i += 1
            else :
                A[k] = R[j]
                j+=1
            k +=1
             
            while i <len(L):
                A[k] = L[i]
                i +=1
                k +=1

            while j <len(R):
                A[k]=R[j]
                j+=1
                k+=1

with open('ad.dat', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]


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
        
        x = int(input("1.) View all Properties  2.) Search based on Price  3.) EXIT "))

        
        if x == 1:
            print(df)
        elif x == 2:
            print(df_sorted)
        elif x == 3:
            print("Exiting the program.")
            break  
        else:
            print("Invalid option. Please choose a valid option.")