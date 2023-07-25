def choose_topic(userName):
  from fuzzywuzzy import fuzz

  def calculate_similarity(answer, strings):
    similarities = []
    for string in strings:
      similarity = fuzz.token_set_ratio(answer, string)
      similarities.append(similarity)
    return similarities

  variables = {
    '1.theory of probability': '1',
    '2.quantum physics (intuition)': '2',
    '3.sum': '3'
  }

  answer = str(
    input(
      "Choose one of this topics:\n {}.\n *You can select by position number or write ~(simmilar text) but not from 4.5.6.7...etc\n"\
      .format('\n'.join(str(n) for n in variables.keys()))
    ))
  list_keys = list(variables.keys())

  similarities = calculate_similarity(answer, list_keys)
  if max(similarities) > 50:
    most_relevant_index = similarities.index(max(similarities))
    most_relevant_string = list_keys[most_relevant_index]


    for keys, values in variables.items():
      if answer in [keys] + [values]:
        founded_answer = answer
      elif answer:
        founded_answer = most_relevant_string

    def get_keys_by_value(dictionary, value):
      for k, v in dictionary.items():
        if v == value or k == value:
          x = k
      return x

    predict_answer = get_keys_by_value(variables, founded_answer)

    print(f"If I recognize your topic,{userName} we will play {predict_answer}")
    return predict_answer
  else:
    print("Sorry, I didn't understand you. Try again")
    return choose_topic(userName)