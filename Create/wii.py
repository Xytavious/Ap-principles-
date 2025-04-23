import random
with open('junk.txt',"w") as f:
    for _ in range(100): 
        f.write(str(random.randint(50000,500000))+"\n")