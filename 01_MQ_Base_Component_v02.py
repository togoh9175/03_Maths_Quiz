print ()
print ("▁ ▂ ▄ ▅ ▆ ▇ █ ᴡᴇʟᴄᴏᴍᴇ ғᴇʟʟᴏᴡ ʙᴇɪɴɢs █ ▇ ▆ ▅ ▄ ▂ ▁")
print ()


# Functions goes here

def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response
    
    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("                 please answer yes / no")

def instructions ():
  print ()
  print ("     ▁ ▂ ▄ ▅ ▆ ▇ █ ʜᴏᴡ ᴛᴏ ᴘʟᴀʏ █ ▇ ▆ ▅ ▄ ▂ ▁")
  print ()
  print ("   This quiz is not any quiz, Its a math quiz!")
  print ("   There will be math equations for you to answer")
  print ("   This is an addition math quiz, just answer the c")
  print ("   orrect answer and see how many questions you got")
  print ("                       right.")
  return ""


# Main Routine goes here...
played_before = yes_no ("         Have you played the game before? ")

if played_before =="no":
  instructions ()
  
print ()
print ("               Perfect! Lets begin")
print ()
print ("▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌")
print()

# Functions go here

import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

question = "{} + {}".format(num_1, num_2)
user_ans = int(input("{} = ".format(question)))
answer = eval(question)

print(answer) 
