import random
#---------------------------Story Information----------------------------
name = input("What is your name? ")
print("Hello, " + name  + ". I am your Zachary Bank Chatbot") 

def display_menu():
  print("\n ** Zachary Bank**")  
  print("1. checking account balances ") 
  print("2. transferring funds")  
  print("3. providing information about products and services") 


#----------------------------Users choice bank options------------------------
def user_selection():
    global isUsed #global variable isUsed
    user_choice = int(input("\nWhat would you like to do today?(Pick number 1-3) "))
    if user_choice == 1:  #checking account balances
        print("checking account balances..") 
        check_balances()
    elif user_choice == 2:  #transferring funds
        fundTransfer()
    elif user_choice == 3:  #providing information about products and services
        information()
         
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")

      



#--------------------------1-3 Options for users to choose from----------------------
balance = 5000
def check_balances():
   print(balance)

def fundTransfer():
  money_deposit = int(input("\nWhat would you like to do today? Pick an amount under you balances please: " ))
  print("Remaning balance is:")
  print(balance - money_deposit)
  if balance - money_deposit < 0:
    print("You have taken out a loan")

def information():
  info_choice = int(input("\nWhat would you like to know about, 1. for products and 2. for services " ))
  if info_choice == 1:
    print("\nOur products are limitless which you can find more about on our formal website")
  if info_choice == 2:
    print("\nWe currently are rebuilding this location so we will have an operator get back to you shortly")



#------------------------Age Questions --------------------------------  


def myAge(age):
  response3 = random.randint(1, 2)
  
  if age <18:  
      if response3 == 1:
          print("You are young, child lock enabled")
      elif response3 == 2:
          print("That's great that you are still young but a child lock will be initated")        
  elif age >= 18 and age < 100:
      print("An Adult, all controls unlocked")
  else:
      print("Are you sure you're that old. Try again.")
      age2 = int(input("What is your age? "))
      if age2<100:
        print("Okay! This seems more like an accurate age number.")

try:
  age = int(input("\nI need to know what your age is for my databases: "))
except:
  age =5

myAge(age)
display_menu()
user_selection()