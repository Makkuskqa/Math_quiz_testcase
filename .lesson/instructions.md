# Instructions  

  
## Goal of this Project
Now you will create your first Python program. You will create an interactive Quiz Game. This Quiz Game uses everything you learned in the Basiscs course so far! You will see all the knowledge you learned in action of a real program. Also you will be able to adjust the game yourself. Having your own game in your portfolio will proof that you know the most important basics of Python.


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
- When hitting RUN the program should execute this function.
- The Name of the user should be stored in a variable, so we can reuse it later.


*HINTS:*
- Use the function input()
- Use a variable to store the name
- Use a print function to say hello
- Use the "return" statement to return the name
- Now call the function inside the file main.py inside the function main().
- This is an example where we store the returned value of the function in the variable "text":
```python
def some_function():
  text = "i am a function"
  return text

text = some_function()

```


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
- When hitting RUN the program should execute this function.
- The topic the user chose should then be stored in a variable so we can reuse it later.
- When asking the user to choose for a topic, include his name in your question.


*HINTS:*
- Save the 3 topics in a list
- Use the function input() to ask the user for a topic
- Use a variable to store the topic the user chose
- To check if the user chose one of the 3 possible topic options use a "if statement"
- To ask the question again until the user chooses one of the 3 topics use a "while loop"
- Use the "return" statement to return the topic
- The name of the user should be already stored in a variable. Use this variable as an input to the function. Then use it in your question.


*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition


## 4. Function should give us random question and answer
*TASKS:*
<br />Go into the file module/quiz.py.
<br />Use the function "get_questions_and_answers"
<br />Now fill out the function. The function should:
- This function should return a random question and answer of the topic that the user chose
- The questions should be an easy mathematical equations for the topic he chose. (e.g 2 - 2 for the topic "substraction")
- For every topic there should be at least 2 questions with answer.
- As an answer use a number as a string. For example "2" (with the quotation marks).
- When hitting RUN the program should execute this function.
- Save the Set of the random question and answer in a variable so we can reuse it later.


*HINTS:*
- Use the variable "topic" as an input parameter. You saved this value before in the variable "topic".
- To save all the questions and answers we will use a nested arrays.
- First of all create a dictionary with a key for each topic
- The value for each key should be a list
- In this list you will have Sets with 2 values. The first value is the question. The second value is the right answer. This set can look like this: ("1 + 10", "11")
- To get a random element of a list (to get a random question of one topic) you can use the "choice" function:
```python
from random import choice
colours = ["blue", "yellow", "green"]
print(choice(colours))
```
- You can save the set of question and answer like this: question_and_answer = get_questions_and_answers(topic)



*Learn Resources:*
- Check out following chapters of the Python Basics course: variables, functions, lists, sets, dictionaries


## 5. Ask the user the question and check if answer is correct
*TASKS:*
<br />Go into the file module/quiz.py.
<br />Use the function "answer_question"
<br />Now fill out the function. The function should:
- Ask the user the question that was chosen by the function before (get_questions_and_answers)
- Let the user write an answer
- Check if the answer of the user matches the right answer.
- Let him know if the answer was correct or not.
- If it was correct the function should return the bollean True. If its wrong it should return the boolean False.
- When hitting RUN the program should execute this function.
- Save the returned boolean value (True or False) in a variable, so we can reuse it later.


*HINTS:*
- Store the question and the answer in a seperate variable. The set has 2 elements. To get for example the first value of the set (question) do this:
```python
some_set = ("question", "answer")
question = some_set[0]
```
- Print the Question
- Use the input() function to ask the user for the answer
- Use an If Else Condition to check if the input of the user is the same as the answer.
- Use the print() statement to tell the user if he was right or not.


*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition, sets

## 6. Count the score of the user
*TASKS:*
- For that tasks we only have to work in the function main() in the file main.py
- Everytime the user gets a right answer he should get a point.
- At the end of the game we want to print out the score of the user.

*HINTS:*
- In the beginning of the game define a variable score with the value of 0
- In the task before we have saved a boolean which tells us if the answer was right (True) or not (False).
- Use an if else condition to check the boolean value.
- If its True then add 1 to our score variable.

*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, if else condition

## 7. Play many rounds
*TASKS:*
- For that tasks we only have to work in the function main() in the file main.py
- The game should go over many rounds (at least 2)
- At the beginning of the round let the user know in which round he is


*HINTS:*
- Like with the score before, define a variable for rounds. This one should have the value 1 at the beginning.
- Now use a while loop to play the same game many times
- At the end of the loop at 1 to the round number
- At the beginning of the loop use a condition which checks for the round number. If you want 2 rounds you can say "while rounds<=2:"


*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, while loop






## 8. Add Function with all the Print Statements
The Quiz has a lot of Print Statements that the user sees in the console.
To avoid to write all the print statement in our "main.py" we will outsource them into a function. This function we then can call and tell it which print block we want to use. A Print block are just many print commands in a row that we want to use together. 
For example:
```python
print("hello")
print("how are you?")
```


*TASKS:*
<br />Go into the file module/print_functions.py.
<br />Use the function "print_function"
<br />Now fill out the function. The function should:

- Have an Input parameter "category" that tells what we want to Print
- Depending of the value of "category" different print statements should be printed.
- For the following categories we want a print statement for the user:
1) welcome (welcome message in the beginning)
2) correct_answer (Let the user know he made the correct answer)
3) wrong answer (Let the user know he made a wrong answer)
4) exit (Let the user know the program ended)

- Add 2 more input parameters: round and score
- Make those parameters optional. That means when the function is called the parameters can be set but dont have to be set.
- Now we want to add 2 more Print blocks. But those Print statements will include the parameters "round" and "score"
1) round (Let the user know in which round he is) 
2) score (Let the user know hom much he scored)
- Everywhere in the program where we have a print function replace it with a print block of this function.
For example instead of having this:
```python
def main():
  print("Welcome to our game")
  print("Have FUN!")
```
Now we can replace it with sth. like this:
```python
def main():
  print_function("welcome")
  ```


*HINTS:*
- Use If Else Blocks to check which value the input parameter "category" has. Then execute the matching Print Block
- To add a variable inside a print function you can use "formatting". For that put a "f" before the string. Than inside curley brackets you can insert the variable.
For example:
```python
name = "peter"
print(f"how are you {name}?")
```
- To make an input paramter optional define the parameter as None. If the function now can be called with this input parameter or without.
```python
def some_function(this_parameter_is_required, this_not=None):
```

*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, if else condition

## 9. Improve the Game
*TASKS:*:
- Add a replay functionality for the user after the game is finished
- Add settings in the beginning. The user should be able to choose how many rounds he wants to play
- In the settings add the difficulty of the game. Depending on it, the user should get an "easy" or a "difficult" question.
- We can persist the score of each user and write it into a file. Also add the date of the achieved score. In the beginning of each game show the ranking of all players. You dont know how to read and write to files yet. For that use google/chatgpt. Try to find out how to use the function "with open()"
  

## 10. Implement your own Ideas to Improve the Game
You have already created a simple quiz game. 
Now, i want you to come up with your own ideas to improve the quiz game. You will learn to estimate which ideas are easy to implement and which are not worth the time. The goal should be to add as much value as possible with as little effort as possible.


*TASKS:*:
- I want you to come up with 3-5 ideas how to improve the quiz game.
- Improvement could be in user experience, error resistance, game logic, code style and more
- If you have a great idea, but dont know how to implement it, ask your teacher for support
- implement those ideas
