print("Welcome to quizr")

play=input("Do you wanna start the game?")

if play.lower()!="yes":
    quit()
   
print("okay!! lets play:)")
score = 0

ans = input("How many stripes are there on us flag? ")
if ans == "13":
    print('Correct!')
    score+=1
else:
      print('Incorrect!')
      
ans = input("Captial of canada? ")
if ans == "Ottawa":
    print('Correct!')
    score += 1
else:
      print('Incorrect!')
      
ans = input("name the longest river in the world? ")
if ans == "Nile":
    print('Correct!')
    score += 1
else:
      print('Incorrect!')
      
ans = input("National animal of India? ")
if ans == "Tiger":
    print('Correct!')
    score += 1
else:
      print('Incorrect!')
      
print(f"you got"  + str(score) +  "questions correct" )
print(f"you got" + (str(score/4)*100 ) + "%")
print("Well played!! ")
print(f"THANK YOU FOR PARTICIPATING IN QUIZ!!!")
