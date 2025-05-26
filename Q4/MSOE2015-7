def calc(n):
    
    triangle = []
    i = 0
    while True:
        t = int(i * (i + 1) / 2)
        if t > n:
            break
        triangle.append(t)
        i += 1
    return triangle

def find(n):
    triangle = calc(n)
    length = len(triangle)

    for i in range(length):
        for j in range(length):
            for k in range(length):
                if triangle[i] + triangle[j] + triangle[k] == n:
                    return triangle[i], triangle[j], triangle[k]
    return None

def main():
    n = int(input("Enter a number: "))
    s = find(n)
    if s:
        print(f"{n} can be partitioned as: {s[0]}, {s[1]}, {s[2]}")
    else:
        print("No valid partition.")

if __name__ == "__main__":
    main()