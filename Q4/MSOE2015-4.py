nums =[]
print("Enter 10 numers")
for i in range(10):
    n = float(input("Enter Number "))
    nums.append(n)

    if i>=2:
        s = sorted(nums, reverse= True)
        print("thrid latgest so far is: ", s[2])
