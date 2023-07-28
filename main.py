# Ashley Darling
# 11/11/2022
# Tortoise & Hare Project
'''

1) Create variables,
  -Import random
  - variables for tortoise and Hare
2) Creating a random function for each variable
   establishing a main function
   creating a turtle function 
   creating a hare function

3) Create while loops
   the while loop displays the limit and determines the winner of the program between the tortoise and hare
   also displays the action and location of the tortoise and hare

4) Create output statements for every randomization
 each output statement displays 
5) create if statements in relation to the print statements and while loops
  - display time elapsed and results each turn
  -  Counter for increments
  - making an if statement for who has won the race (> 70 )

6) add a sleep function  
the sleep function displays the delaying time the program should print each time, position, and reaction of the tortoise and the hare

'''
# Function of the tortoise looping through the randomization of numbers and displaying the out results if each number
def Turtle():
  i = random.randint(1,10)
  if i <= 5:
    print("Tortoise is flying! Fast Plod!")
    return 3
  elif i == 6 or i == 7:
    print("HE SLIPPED! THE TORTOISE HAS SLIPPED!!!")
    return -6
  elif i == 8 or i == 9 or i == 10:
    print("SLOW PLOD! TORTOISE IS PLODDIG AHEAD... SLOWLY...")
    return 1


  # Function of the Hare looping through the randomization of numbers and displaying the output results of each number
def Har():
  i = random.randint(1,10)
  if i <= 2:
    print("THE HARE IS SLEEP!")
    return 0
  elif i == 3 or i == 4:
    print("THE HARE MADE A BIG HOP!!")
    return 9
  elif i == 5:
    print("BiG SLIP!!!!")
    return -12
  elif i == 6 or i == 7 or i == 8:
    print("THE HARE MADE A SMALL GAIN?SMALL HOP!!!")
    return 1 
  elif i == 9 or i == 10:
    print("SMALL SLIP!!!!!!!")
    return -2
    
import random # importing the random number for the tortoise and hare
import time # importing the time taking note of how much time has passed
def main():
  tortoise = 1
  hare = 1
  counter = 0
  # Startof the program
  print("WELCOME TO THE ANNUAL RACE!")
  print("READY....")
  print("SET......")
  print("BANG  !!!!!")
  print("AND THEY'RE OFF !!!!!! ")


  #This represents and determines the winner of the program   as well as the positioning for each animal
  while tortoise < 70 and hare < 70:
    time.sleep(1) # makes the system lag each output by 1 second incraments
    tortoise += Turtle()
    hare += Har()
    counter += 1

    if tortoise < 0:
      tortoise = 1
  
    if hare < 0:
      hare = 1
    print("The position of the Hare is: ", hare)
    print("The position of the Tortoise is: ", tortoise)
    print("The time is ", counter, "seconds")

    if tortoise == hare:
      print("TORTOISE BIT HARE !!!!!OUUUUCCCCH!!!!!!!!")

    if tortoise >= 70:
      print("YAAAY!!! TORTOISE WINS!!!!")
      break

    elif hare >= 70:
      print("HARE WINS. COOL.")
      break

    elif tortoise >= 70 and hare >= 70:
      print("its a tie. ")
      break

main()