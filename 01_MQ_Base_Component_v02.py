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
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before.
# if 'yes', show instructions


# ask user for # of rounds then loop
rounds_played = 0

rounds_lost = 0
rounds_drawn = 0

game_summary = []

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    # Start of Game Play Loop
    # Rounds Heading
    print()
    if rounds == "":
        heading = "continuous Mode:  "  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
    print(heading)

    choose_instructions = "please choose rock (r) paper (p) or scissors (s) or 'xxx to exit "
    choose_error = "please choose from rock paper scissors (or xxx to quit)"
    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instructions, rps_list,
                            choose_error)
    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("comp choice", comp_choice)

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "it's a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice,
                                              comp_choice, result)
    # end game if exit code is typed
    if user_choice == "xxx":
        break
    #  ***** rest of loop / game *****
    print("you choose {}".format(user_choice))

    # output results
    print(feedback)
    summary_statement = "Round {}: {}".format(rounds_played + 1, feedback)
    game_summary.append(summary_statement)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# ask user if they want to see their game history


rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *******")
for game in game_summary:
    print(game)

print()

# display game stats when % values to the nearest whole number
print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%)\nloss: {}, "
      "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won,
                                              percent_win,
                                              rounds_lost,
                                              percent_lose,
                                              rounds_drawn,
                                              percent_tie,))
# if 'yes' show game history

# show game statistics
# Quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of game statements
print()
print('***** End Game Summary ******')
print("won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks For Playing")