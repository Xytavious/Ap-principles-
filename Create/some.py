# Rental Property Manager or Inventory Manager
# rental properties, tenants, and rent due
# stock levels, sales, and reorders
# need 2 functions 
#make table with surch alg to pull data 
# make options to add data /
import pandas as pd
from Sort import mergesort

def main():
    
    with open("ad.dat", 'r') as f: 
        lines =f.readlines()
    li =[]
    for i in range(0, len(lines), 7):  #links house information all together 
      if i + 7 < len(lines):  #fixes out of bounds
        Adress = lines[i].strip()
        Street = lines[i+1].strip()
        P = lines[i+2].strip()
        B = lines[i+3].strip()
        Bath = lines[i+4].strip()
        sqr = lines[i+5].strip()
        lot = lines[i+6].strip()
        li.append((Adress,Street,P,B,Bath,sqr,lot)) 
        
    x = input("1.) Veiw all Properties  2.) Search based on street 3.) Manage properties ")
    if x == "1":
        
        print("hi")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        
        df = pd.DataFrame(li, columns=["Address", "Street\t", "Price\t", "Bedrooms\t", "Bathrooms\t", "Square Feet\t", "Lot Size"])

    
        print(df.to_string(index=False))
        
    elif x =="2":
        user = int(input("Entered desired Pice. "))
        
        
        for i in range(0,len(li),3):
            print(P)
            #min_dif = min(abs(li[2]-user == min_dif))
            #cl= [li for li in li if abs(li[2]-user)]
            #if user == li[i]:
            #    we = []
            #    we.append(li.index(i))
        #print(we)
        #c= mergesort
        #c(li)
        #print(li)

        
    #properties = 0
    #tenants = 0
    #rent_due =0
    #print(li)
# make algorithm to sort and catogrize 




#def h():
   # j[6][6] = {213456},{465879}


if __name__=="__main__":
    main()