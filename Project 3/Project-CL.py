#1. ask user qestion from a array
#2. recive user input
#3. compare user input to answaer for the given array
#4. display users answer 
# note: use true or false to detemin 
# need algorithm
# make an list of acceptible answers and use the algorithm to for that: IKD why you would need an algorithm in the first place /
#5. Display correct or incorrect 
#6. Display answer
#7. note make score traker each correct answer gives 1 point/ with multipler for each qestion in a row: could use algorithm for this 

import random
 
# Trivia questions and answers 
#lines = f.readlines
#get random qestoin from the data file 

wow = 0 # attempt to make a loop that stops when player wants to stop playing
score = 0
while True:
    
    with open("Triv.dat", 'r') as f: 
        lines =f.readlines()

    
    qa = []

    for i in range(0, len(lines), 2): # link the answe and gestions together
        question = lines[i].strip()
        answer = lines[i + 1].strip()
        qa.append((question, answer))
        

    selc_qa = random.choice(qa)

    print("Question:", selc_qa[0])
    user_answer = input("Enter Answer: ")
    if user_answer.strip().lower() == selc_qa[1].strip().lower():
        print("Correct ;)")
        score +=1
    else:
        print("Worng!! >:(")
    print("Answer:", selc_qa[1])
        #random.randint(0-len(lines))
        #use 'pop'
    ag = input("play agin? 1.YES  2.NO :( ").strip().lower() #dose not work as intended
    if ag == "no":
        print("Thanks for playing! Goodbye!")
        exit()
    else:
        print(score)
       




#dead code
    
    #make the score variale 
   # # need to loop through the whole process again /