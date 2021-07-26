print ()
print ("▁ ▂ ▄ ▅ ▆ ▇ █ ᴡᴇʟᴄᴏᴍᴇ ғᴇʟʟᴏᴡ ʙᴇɪɴɢs █ ▇ ▆ ▅ ▄ ▂ ▁")
print ()

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


# as user if they have played before.
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
        response = input("How many questions: ")

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


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item
                # output error if item not in list

        print(error)
        print()
# main routine goes here

# list of valid responses
yes_no_list = ["yes", "no"]

# ask user for # of rounds then loop
questions_played = 0
questions_lost = 0

game_summary = []

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    # Start of Game Play Loop
    # Rounds Heading
    print()
    if rounds == "":
        heading = "continuous Mode:  "  "Questions {}".format(questions_played)
    else:
        heading = "Question {} of {}".format(questions_played + 1, rounds)
    print(heading)

    import random

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    questions = "{} + {}".format(num_1, num_2)
    show_questions = "{} = ".format(questions)

   user_ans = check_rounds()

   if user_ans == eval(questions):
     print("correct!".format(user_ans))
     
    answer = eval(question)
    print("answer {}".format(answer))
  
   

    #  ***** rest of loop / game *****
    print("you choose {}".format(user_ans))

    # output results
    summary_statement = "Round {}: {}".format(questions_played + 1, rounds)
    game_summary.append(summary_statement)

    questions_played += 1

    # end game if requested # of rounds has been played
    if questions_played == rounds:
        break


