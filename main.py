import time
from random import randint

won = False
while(won==False):
  print("Tic Tac Toe! \nBy Raven")
  time.sleep(.5)
  askAgain = True
  choice1 = "n"
  
  #Ask Again
  while(askAgain==True):
    print("Would you like to play a game?")
    choice1 = input("Answer (Y/N): ")
    choice1 = choice1.lower()
    if(choice1=="y"):
      askAgain=False
    elif(choice1=="n"):
      print("-------------------- \nWell... Maybe I'll ask again.")
    else:
      print("-------------------- \nI know you said something other than y and n... Wow...")
  
  if(askAgain==False):
    time.sleep(1)
    print("Alright, let's begin.")
    list = [1,2,3,4,5,6,7,8,9]
    time.sleep(1)
  
    #Function
    def chosen(choice3):
      if(choice3 == list[0]):
        list[0] = "x"
      elif(choice3 == list[1]):
        list[1] = "x"
      elif(choice3 == list[2]):
        list[2] = "x"
      elif(choice3 == list[3]):
        list[3] = "x"
      elif(choice3 == list[4]):
        list[4] = "x"
      elif(choice3 == list[5]):
        list[5] = "x"
      elif(choice3 == list[6]):
        list[6] = "x"
      elif(choice3 == list[7]):
        list[7] = "x"
      elif(choice3 == list[8]):
        list[8] = "x"
      
    #Function 2
    def board():
      print(f"-------------------- \n{list[0]} {list[1]} {list[2]} \n{list[3]} {list[4]} {list[5]} \n{list[6]} {list[7]} {list[8]}")
  
        
    #Pick a number
    def pickNum():
      print("Please pick a number")
      choice2 = int(input())
      while(choice2 not in range(1,10)):
        print("Please choose 1, 2, 3, 4, 5, 6 ,7 ,8 or 9")
        choice2 = int(input())
      numValid = False
      
      while(numValid == False):
        if(choice2==1):
          if(list[0]=="x") or (list[0]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True
            
        elif(choice2==2):
          if(list[1]=="x") or (list[1]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True
            
        elif(choice2==3):
          if(list[2]=="x") or (list[2]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==4):
          if(list[3]=="x") or (list[3]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==5):
          if(list[4]=="x") or (list[4]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==6):
          if(list[5]=="x") or (list[5]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==7):
          if(list[6]=="x") or (list[6]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==8):
          if(list[7]=="x") or (list[7]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

        elif(choice2==9):
          if(list[8]=="x") or (list[8]=="o"):
            print("Please pick again! That number can't be put on the board!")
            choice2 = int(input())
          else:
            numValid = True

            
      print(f"Alright! {choice2} it is!")
      chosen(choice2)
      board()

    board()
    pickNum()
    
    def compValidC():
      compChoice = randint(1,9)
      compValid = False
      while(compValid==False):
        
        if(compChoice == 1):
          if(list[0] == "o") or (list[0] == "x"):
            compChoice = randint(1,10)
          else:
            list[0] = "o"
            compValid = True
            print("Computer chose 1")
            
        elif(compChoice == 2):
          if(list[1] == "o") or (list[1] == "x"):
            compChoice = randint(1,10)
          else:
            list[1] = "o"
            compValid = True
            print("Computer chose 2")
            
        elif(compChoice == 3):
          if(list[2] == "o") or (list[2] == "x"):
            compChoice = randint(1,10)
          else:
            list[2] = "o"
            compValid = True
            print("Computer chose 3")
            
        elif(compChoice == 4):
          if(list[3] == "o") or (list[3] == "x"):
            compChoice = randint(1,10)
          else:
            list[3] = "o"
            compValid = True
            print("Computer chose 4")
            
        elif(compChoice == 5):
          if(list[4] == "o") or (list[4] == "x"):
            compChoice = randint(1,10)
          else:
            list[4] = "o"
            compValid = True
            print("Computer chose 5")
            
        elif(compChoice == 6):
          if(list[5] == "o") or (list[5] == "x"):
            compChoice = randint(1,10)
          else:
            list[5] = "o"
            compValid = True
            print("Computer chose 6")
            
        elif(compChoice == 7):
          if(list[6] == "o") or (list[6] == "x"):
            compChoice = randint(1,10)
          else:
            list[6] = "o"
            compValid = True
            print("Computer chose 7")
            
        elif(compChoice == 8):
          if(list[7] == "o") or (list[7] == "x"):
            compChoice = randint(1,10)
          else:
            list[7] = "o"
            compValid = True
            print("Computer chose 8")
            
        elif(compChoice == 9):
          if(list[8] == "o") or (list[8] == "x"):
            compChoice = randint(1,10)
          else:
            list[8] = "o"
            compValid = True
            print("Computer chose 9")

    #Check Win
    def checkwin():
      if(list[0] == list[1]) and (list[1] == list[2]):
        if(list[0]=="o"):
          print("Computer Won!")
        elif(list[0]=="x"):
          print("You Won!")
          won = True
          
          
      elif(list[0] == list[3]) and (list[3] == list[6]):
        if(list[0]=="o"):
          print("Computer Won!")
        elif(list[0]=="x"):
          print("You Won!")
          won = True
          
          
      elif(list[2] == list[5]) and (list[5] == list[8]):
        if(list[2]=="o"):
          print("Computer Won!")
        elif(list[2]=="x"):
          print("You Won!")
          won = True
          
          
      elif(list[6] == list[7]) and (list[7] == list[8]):
        if(list[6]=="o"):
          print("Computer Won!")
        elif(list[6]=="x"):
          print("You Won!")
          won = True
          
          
      elif(list[0] == list[4]) and (list[4] == list[8]):
        if(list[0]=="o"):
          print("Computer Won!")
        elif(list[0]=="x"):
          print("You Won!")
          won = True
          
          
      elif(list[2] == list[4]) and (list[4] == list[6]):
        if(list[2]=="o"):
          print("Computer Won!")
        elif(list[2]=="x"):
          print("You Won!")
          won = True
          

    while(won==False):
      compValidC()
      board()
      checkwin()

      pickNum()
      checkwin()

      time.sleep(1)
      if(list[0]=="x") or (list[0] == "o"):
        if(list[1]=="x") or (list[1] == "o"):
          if(list[2]=="x") or (list[2] == "o"):
            if(list[3]=="x") or (list[3] == "o"):
              if(list[4]=="x") or (list[4] == "o"):
                if(list[5]=="x") or (list[5] == "o"):
                  if(list[6]=="x") or (list[6] == "o"):
                    if(list[7]=="x") or (list[7] == "o"):
                      if(list[8]=="x") or (list[8] == "o"):
                        print("It's a tie! How did you not win against my bot.")
                        won = True
                        break