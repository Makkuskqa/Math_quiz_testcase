from random import choice


def get_questions_and_answers(predict_answer):
  """Fill out the function. """
  print('Okay ')

  Select = {
    '1.theory of probability':
    [('If you randomly shuffle a deck of cards, what is the probability that the cards will be ordered exactly as they were before the shuffle?',
      '50/50'),
     ('What is the probability that you will drop your toast and it will  land butter-side up?',
      '50/50')],
    '2.quantum physics (intuition)':
    [("If Schrödinger's cat was put in a box with a quantum physicist, would the cat be both alive and dead until observed?",
      'yes'), ('Can a particle be in two places at the same time?', 'yes')],
    '3.sum': [('2+0*2', '2'), ('2/0,1', '20')]
  }

  for k, v in Select.items():
    if k == predict_answer:
      question_answer = choice(v)
      return question_answer


def answer_question(question_answer):
  """Fill out the function. """
  question = question_answer[0]
  print(question)
  answer = str(
    input(
      f"Input answer( Reply should be very easy, like: 50/50, yes, or math result)\n"
    ))
  if answer == question_answer[1]:
    print('Congrats +1 score')
    return True
  else:
    print('maybe you are correct on your mind, but answer was more correct')
    return False


#print(f"Your scores: {user_scores}")
