

print("enter length ")
len = readline()
n1 = parse(Int64,len)

print("enter width ")
wid = readline()
n2 = parse(Int,wid)

area = n1 * n2 
perim = 2 *(n1 + n2)

println("The area is: ", area)
println("The perimiter is: ", perim)
/*
enter length 2
enter width 2
The area is: 4
The perimiter is: 8
*/