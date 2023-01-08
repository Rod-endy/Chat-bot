import random
#---------------------------Story Information----------------------------
name = input("What is your name? ")
print("Hello, " + name  + ". I am your personal AI ") 
botName = input("What would you like to name me: ")
print("My name is " + botName + " thank you for my name")

#------------------------Feeling/Emotion Questions ----------------------

def myFeeling(feeling):
  randresp1 = random.randint(1,2)
  randresp2 = random.randint(1,2)
  goodFeelings = ["happy","delighted" , "great" , "okay", "ok" ,"good" , "well" , "nice"]
  badFeelings = ["sad","down","depressed", "unwell","unhappy" ,"bad","not good"]
  
  if feeling in goodFeelings:
      if randresp1 == 1:
          print("Good to hear!")
      elif randresp1 == 2:
          print("Great!")
  elif  feeling in badFeelings:
      if randresp2 == 1:
          print("I'm sorry to hear that!")
          print("Keep your head up, I'm sure things will smoothen out soon enough.")
      elif randresp2 == 2:
          print("I'm sorry for you!")
          wrong = input("What's wrong? ")
          if wrong == "nothing" or wrong == "don't want to share." or wrong == "It's okay":
              print("Alright, no worries.")
          else:
              print("We don't have to talk about it if you don't want to. \n Let's move on.")
  else:
      print("Alright. Let's continue.")

  
feeling = input("\nHow are you feeling today? ").lower()
myFeeling(feeling)

#------------------------Age Questions ----------------------  


def myAge(age):
  response3 = random.randint(1, 2)
  
  if age <14:
      if response3 == 1:
          print("You are young, child lock enabled")
      elif response3 == 2:
          print("That's great that you are still young but a child lock will be initated")        
  elif age >= 14 and age < 18:
      print("You are a teen, great.")
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