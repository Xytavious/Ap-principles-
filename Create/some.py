# Rental Property Manager or Inventory Manager
# rental properties, tenants, and rent due
# stock levels, sales, and reorders
# need 2 functions 
#make table with surch alg to pull data 
# make options to add data /
import pandas as pd
from Sort import mergesort
ft = pd.DataFrame()
def main():
    
    with open("ad.dat", 'r') as f: 
        lines =f.readlines()
    li =[]
    for i in range(0, len(lines), 6):  #links house information all together 
      Adress = lines[i].strip()
      Street = lines[i+1].strip()
      PB = lines[i+2].strip()
      Bath = lines[i+3].strip()
      sqr = lines[i+4].strip()
      lot = lines[i+5].strip()
      li.append((Adress,Street,PB,Bath,sqr,lot)) 

    print(li)
    x = input("1.) Veiw all Properties  2.) Search based on street 3.) Manage properties ")
    if x ==1:
        ft['Adress'] = li
        ft['Street'] = Street
        ft['Bedrooms']= 0
        ft['Baths'] = Bath
        print(ft)
    elif x ==2:
        c= 0

        
    #properties = 0
    #tenants = 0
    #rent_due =0
    #print(li)
# make algorithm to sort and catogrize 




#def h():
   # j[6][6] = {213456},{465879}


if __name__=="__main__":
    main()