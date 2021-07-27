
import random

  num_1 = random.randint(1, 10)
  num_2 = random.randint(1, 10)

  question = "{} + {}".format(num_1, num_2)
  show_question = "{} = ".format(show_question)

  user_ans = num_check(show_question,"xxx")
  if user_ans == "xxx":
    break
  if user_ans == eval(questions):
    print("correct!".format(user_ans))

  answer = eval(question)
  print("answer {}".format(answer))
  num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    questions = "{} + {}".format(num_1, num_2)
    show_questions = "{} = ".format(questions)
