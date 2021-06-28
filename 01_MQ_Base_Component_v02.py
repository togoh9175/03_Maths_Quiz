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
def check_rounds():
    while True:
        response = input("How many questions would you like: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # if response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response
