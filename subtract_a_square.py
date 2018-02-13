import math

pile =int(input("enter the pile of your choice: "))
print(pile)
while(True):
    p1Input=int(input("enter your number p1: "))
    square=math.sqrt(p1Input)
    floor =int(square)
    
    if(square !=floor):
        print("not a square number!")
        p1Input=int(input("enter again p1:"))
        
    if(p1Input>pile):
        print("number is lager than the pile!")
        p1Input=int(input("enter again p1:"))

    pile-=p1Input
    print(pile)
    if(pile==0):
        print("player 1 won !")
        break


    p2Input=int(input("enter your number p2: "))
    square=math.sqrt(p2Input)
    floor =int(square)
    
    if(square !=floor):
        print("not a square number!")
        p2Input=int(input("enter again p2:"))
        
    if(p2Input>pile):
        print("number is lager than the pile!")
        p2Input=int(input("enter again p2:"))

    pile-=p2Input
    print(pile)
    if(pile==0):
        print("player 2 won !")
        break
    
