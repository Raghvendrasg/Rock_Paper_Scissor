from operator import truediv
import random
from tkinter import Y
bot_choice=['Rock','Paper','Scissor']
while True:
    print("Rock Paper Scissor Game")
    youwin,computerwin=0,0
    for i in range(1,4):
        print("Round",i,"Start :")
        print("Please Select any one option:")
        print("1:Rock","2:Paper","3:Scissor",sep="\n")
        Yourchoice=int(input())
        if Yourchoice==1:
            print("You Select Rock")
            Yourchoice="Rock"
        elif Yourchoice==2:
            print("You Select Paper")
            Yourchoice="Paper"
        elif Yourchoice==3:
            print("You select Scissor")
            Yourchoice="Scissor"
        else:
            print("Invalid Choice")
            break
        computerchoice=random.choice(bot_choice)
        print("Computer Select :",computerchoice)
        if Yourchoice==computerchoice:
            youwin+=1
            computerwin+=1
            print("This Round is Draw :")
        elif (Yourchoice=="Paper" and computerchoice=="Rock") or (Yourchoice=="Rock" and computerchoice=="Scissor") or(Yourchoice=="Scissor" and computerchoice=="Paper"):
            youwin+=1
            print("You win this Round")
        else:
            computerwin+=1
            print("Computer win this Round")
    if youwin>computerwin:
        print("You win the Game")
        print("Score is :","Your Score :",youwin,"computer Score :",computerwin,sep=" ")
    elif computerwin>youwin:
        print("You loose the Game.Computer Win the Game:")
        print("Score is :","Your Score :",youwin,"computer Score :",computerwin,sep=" ")
    else:
        print("Match drawn")
        print("Score is :","Your Score :",youwin,"computer Score :",computerwin,sep=" ")
    user_choice=input("Want to play again ?(YES/Exit)")
    if user_choice=="YES" or user_choice=="yes" or user_choice=="Yes":
        continue
    else:
        break;





