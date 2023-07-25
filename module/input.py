
def user_input(check_name):
  
  userName = str(
    input("Hey, human, who are you? Give me your name pls\n"))
  
  if not userName:
    print('omg you are noob, pls try to print your name if it"s not too hard for you')
    return user_input(check_name)
  
  elif userName in check_name:
    print('this username is taken')
    return user_input(check_name)
    
  else:
    print(f"you're welcome  {userName} 🤝🫡")

  return userName
