import random

randno =random.randint(1,100)
# print(randno)
userInput = None
guess=0
while(userInput!=randno) :
    
    userInput=int(input("Enter The Number : "))
    guess+=1
    if (userInput>randno) :
        print("You Guessed Higher Number, Guess The Low one")
    elif (userInput<randno) :
        print("You Guessed the Lower Number, Guess The High One")
    else :
        print("You Guessed it Right in",guess,"Guesses")

with open("main/highscore.txt") as f :
    a=int(f.read())
if guess<a : 
    print("Congratulations,You Created New High Score as preivious One was ",a)
    with open("main/highscore.txt",'w') as f :
        f.write(f"Highest Score of Guessing Number is {guess}")