
def check_rounds():...


# Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper " \
"(p) or scissors (s)"

#Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

  # Rounds Heading
  print()
  if rounds == "":
    heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    print(heading)
    choose = input("{} or 'xxx' to end:".format(choose_instruction))
    if choose =="xxx":
      break
  else:
    heading = "Rounds {} of {}".format(rounds_played + 1, rounds)
    print(heading)
    choose = input(choose_instruction)
    if rounds_played == rounds - 1:
      end_game = "yes"
  


# rest of loop / game
print("You chose {}")