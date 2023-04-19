# Instructions  

  
## Goal of this Project
Now you will create your first Python program. You will create an interactive Quiz Game. This   Quiz Game uses everything you learned in the Basiscs course so far! You will see all the knowledge you learned in action of a real program. Also you will be able to adjust the game yourself. Having your own game in your portfolio will proof that you know the most important basics of Python.


## Structure of the Program

Basically the program will ask the user questions to different topics. 
We will check if the provided answer was correct. The score of the user will be saved in a ranking file. If you want to see the whole program, check out the final version.


## LETS GET STARTED

When writing a program you want to cut the logic into many small pieces. For that we create sperate modules. Here we have functions that we will import into our program. I have already created the files and functions for you. You will need to fill the functions out and then integrate them into the main file.

## 1. RUN the program
In order to RUN the program you have to click on the Green RUN button at the top. When you click this button, the file "main.py" will be executed.
Now you should see "Welcome to our Quiz" in the Console.

*TASKS:*
- Change the welcome message of the user and run the program again.



## 2. Input from the User

*TASKS:*
<br />Go into the file module/input.py
<br />Use the function "user_input"
<br />The function should:
- ask the user for his name. 
- Say hello to the user using his name.
- The function should return the name.


*HINTS:*
- Use the function input()
- Use a variable to store the name
- Use a print function to say hello
- Use the "return" statement to return the name

*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions



## 3. User should choose a topic
*TASKS:*
<br />Go into the file module/topic.py.
<br />Use the function "choose_topic"
<br />The function should:
- Have 3 different mathematical topics (e.g addition) the user can choose from
- The user should be asked to choose one of those 3 topics.
- If the user input is not one of those 3 topics, he should be asked again until he gives one of those 3 topics as an input.
- The function should return the topic the user chose

*HINTS:*
- Save the 3 topics in a list
- Use the function input() to ask the user for a topic
- Use a variable to store the topic the user chose
- To check if the user chose one of the 3 possible topic options use a "if statement"
- To ask the question again until the user chooses one of the 3 topics use a "while loop"
- Use the "return" statement to return the topic



*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition


## 4. User should answer a question
*TASKS:*
<br />Go into the file module/quiz.py.
<br />Use the function "get_questions_and_answers"
<br />Now fill out the function. The function should:
- The user should get a question for the topic he chose.
- For every topic there should be at least 2 questions with answer.
- As an answer use a number as a string. For example "2" (with the brackets).
- The user should get a random question of the topic he chose.


*HINTS:*
- Use the variable "topic" as an input parameter. You saved this value before in the variable "topic".
- To save all the questions and answers we will use nested arrays.
- First of all create a Dictionary with a key for each topic
- The value for each key should be a list
- In this list you will have Sets with 2 values. The first value is the question. The second value is the right answer. This set can look like this: ("1 + 10", "11")
- To get a random element of a list (to get a random question of one topic) you can use the "choice" function:
```python
from random import choice
colours = ["blue", "yellow", "green"]
print(choice(colours))
```
- The function should return a set with one question and one answer, e.g ("1 + 10", "11")

*Learn Resources:*
- Check out following chapters of the Python Basics course: variables, functions, lists, sets, dictionaries


## 4. Check if answer is correct
*TASKS:*
<br />Go into the file module/quiz.py.
<br />Fill out the function "answer_question"
<br />Now fill out the function. The function should:
- Call the function "get_questions_and_answers" to get a Set of question and answer
- Ask the user the question.
- Check if the answer of the user matches the right answer.
- Let him know if the answer was correct.


*HINTS:*
- You can save the set of question and answer like this: question_and_answer = get_questions_and_answers(topic)
- Now store the question and the answer in a seperate variable
- Print the Question
- Use the input() function to ask the user for the answer
- Use an If Else Condition to check if the input of the user is the same as the answer.
- Use the print() statement to tell the user if he was right or not.


*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition, sets

