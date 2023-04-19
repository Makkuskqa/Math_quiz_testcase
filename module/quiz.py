from random import choice


def get_questions_and_answers(topic):
  """Fill out the function. """


def answer_question(name: str, topic: str) -> bool:
    question_and_answer = get_questions_and_answers(topic)
    question = question_and_answer[0]
    correct_answer = question_and_answer[1]
    print(f"--- {name}, What is the result of following math equation: ---")
    print(question + "\n")
    user_answer = input("Enter a whole number from 0-100: ")
    if user_answer == correct_answer:
        print("\n--> The answer is correct.")
        return True
    else:
        print(f"\n--> The answer is incorrect. The correct answer is: {correct_answer}")
        return False