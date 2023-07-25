from random import random
from random import randint
from random import choice
from module.print_functions import print_function
from module.quiz import answer_question, get_questions_and_answers
from module.topic import choose_topic
from module.input import user_input
import datetime
import pandas as pd




def main():
  """
  Here we will have the logic of the game.
  Here we will use the imported functions that we will create.
  """
  user_scores = 0
  game_round = 1
  print_function(hello=True)
  check_name = print_function(start=True)
  userName = user_input(check_name)

  how_many_Rounds_Play = int(input(f"How many round you want to play?\n"))
  print_function(starting_dasboard=True)
  while game_round <= how_many_Rounds_Play:
    print_function(game_round=game_round)
    predict_answer = choose_topic(userName)
    correctness_of_answer = answer_question(get_questions_and_answers(predict_answer))

    if correctness_of_answer:
      user_scores += 1
    else:
      user_scores -= 1
    print_function(user_scores=user_scores)
    game_round = game_round + 1

  time = datetime.datetime.now()
  players = pd.DataFrame({
    'player': [userName],
    'rounds': [game_round],
    'scores': [user_scores],
    'Time': [time]
  })
  players = players.sort_values(by='scores', ascending=False)
  players.to_csv('module/playersResult.txt',
                 mode='a',
                 index=False,
                 sep='\t',
                 header=False)

  print_function(game_vin=1)
  print_function(userName=userName, time=time)



  we_continue = print_function(next_round=True)

  if we_continue == 'continue':
    while True:
      def continue_play(players):
        from module.next_pack_questions import new_round_new_questions
        players = new_round_new_questions(players)

        players.to_csv('module/playersResult.txt',
                    mode='a',
                    index=False,
                    sep='\t',
                    header=False)
                    
        print_function(userName=userName, time=time)
        return players
      players = continue_play(players)

      we_continue_nex_r = str(input("Do you want play more? *(y/n)"))
      if we_continue_nex_r == 'y':
        print("Okay, lets go!")
        continue_play(players) 
      elif we_continue_nex_r == 'n':
        print("Okay, bye!)")
        break
      else:
        print('Not understand')
        print_function(next_round=True)

  elif we_continue == 'exit':
    print("okay, goodbay")
    

if __name__ == "__main__":
  main()
