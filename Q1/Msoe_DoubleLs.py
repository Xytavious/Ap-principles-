def main(): # run with 'python filename.py' in shell
    word = input("Enter a word ")
    word = word.lower()
    dblcount = 0
    for lcv in range(0,len(word)-1):
        if word[lcv] == word[lcv+1]:
            dblcount += 1
    print(f"{word} containts {dblcount} double leters")        
    pass


if __name__ == "__main__":
    main()    