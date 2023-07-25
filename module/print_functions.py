import pandas as pd
from termcolor import colored
import datetime

def print_function(start = None,
                   hello=None,
                   game_round=None,
                   user_scores=None,
                   game_vin=None,
                   userName=None,
                   time=None,
                  starting_dasboard=None,
                  next_round=None):
  game_history = pd.read_csv('module/playersResult.txt', sep='\t')
                    
  if   start:
    return game_history['player'].tolist()



  if hello:
    print("welcome dude, computer science🍻")



  if starting_dasboard:
    print(f"But first this I want to show you this -> This is your opponents: \n {game_history}")
    



  if game_round:
    print(f"Round number -- {game_round}")



  if user_scores:
    print(f"Your total scores are -- {user_scores}")



  if game_vin:
    print(
      'Congrats you complete this game. Your scores will be saved, Find yourself')



  if userName and time:
    game_history = pd.read_csv('module/playersResult.txt', sep='\t')
    game_history = game_history.drop_duplicates(subset='player', keep='last')
    row_index = game_history[game_history['Time'] == str(time)].index
    def highlight_row(row):    
      if row.name == row_index:       
        return [colored(val, 'yellow') for val in row]
      return row
    highlighted_df = game_history.apply(highlight_row, axis=1)
    print(highlighted_df)
    print('The problem with normal formating string is that in replit not working display() from Ipython, so better function styler.apply not suitable')



  if next_round:
    next = str(input("we have a new pack with questions for you) do you want to try something new ? * (Y/n)")).lower()
    from fuzzywuzzy import fuzz
    def calculate_similarity(answer, strings):
      similarities = []
      for string in strings:
        similarity = fuzz.token_set_ratio(answer, string)
        similarities.append(similarity)
      return similarities
    list_keys = ['yes', 'no']
    similarities = calculate_similarity(next, list_keys)
    if max(similarities) >= 50:
      most_relevant_index = similarities.index(max(similarities))
      most_relevant_string = list_keys[most_relevant_index]
      if most_relevant_string == 'yes':
        return 'continue'
      else:
        return 'exit'
    else:
      print("I don't understand you")
      return print_function(next_round=1)

