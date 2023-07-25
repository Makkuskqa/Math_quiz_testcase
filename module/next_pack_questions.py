

def new_round_new_questions(players):
    import requests
    import json

    

    def choice_questions(players):
        categories = ['artliterature',
                        'language',
                        'sciencenature',
                        'general',
                        'fooddrink',
                        'peopleplaces',
                        'geography',
                        'historyholidays',
                        'entertainment',
                        'toysgames',
                        'music',
                        'mathematics',
                        'religionmythology',
                        'sportsleisure']

        choice = str(input(f"choose from: {categories}\n")).lower()

        from fuzzywuzzy import fuzz
        def calculate_similarity(answer, strings):
            similarities = []
            for string in strings:
                similarity = fuzz.token_set_ratio(answer, string)
                similarities.append(similarity)
            return similarities

        similarities = calculate_similarity(choice, categories)

        if max(similarities) >= 50:
            most_relevant_index = similarities.index(max(similarities))
            most_relevant_string = categories[most_relevant_index]

            api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(most_relevant_string)
            response = requests.get(api_url, headers={'X-Api-Key': 'PtTVI4uKi0xwUvZ+en3hWQ==4otHBoTdMwWzadZq'})

            if response.status_code == requests.codes.ok:
                dict_question = json.loads(response.text)
                answer = str(input(f"{dict_question[0]['question']}\n"))
                if answer == dict_question[0]['answer']:
                    print("Correct anser, congrats!!!")
                    players[['scores','rounds']] +=1
                    return players
                else:
                    print("wrong answer")
                    players['rounds'] +=1
                    return players

            else:
                print("Error:", response.status_code, response.text)
                print("need restart the game we don't have question right now")

        else:
            print("I dont understand you( try again")
            return choice_questions()

    players = choice_questions(players)
    return players
