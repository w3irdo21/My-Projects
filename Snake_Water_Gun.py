import random 
def game(a,b) :
    if a==b :
        return None
    elif (a=="s" and b=="w") :
        return False
    elif (a=="w" and b=="g") :
        return False
    elif (a=="g" and b=="s") :
        return False
    elif (a=="s" and b=="g") :
        return True
    elif (a=="w" and b=="s") :
        return True
    elif (a=="g" and b=="w") :
        return True
    # elif(b!="s","w","g") :
    #     print("Entered Wrong ")
randno = random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"

User=input("Choose From Snake(s) , Water(w) , Gun(g) :  ")
print(f"You chose {User}")
print(f"Computer chose {comp}")

a= game(comp,User)
if a == None :
    print("Tie")
elif(a==True):
    print("Tou win")
elif(a==False) :
    print("You Lose")
else :
    print("No Result, As You Didn't Enter From The  Reserved Things ")      
