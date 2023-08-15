import random
a = '''
      _ _ _ _ 
----'    _ _ _)_ _ _ _
               _ _ _ _ )_
           _ _ __ _ _ _ _ )
         (_ _ _ _)         
----._ _ _(_ _ _)           
'''

b = '''
      _ _ _ _ 
----'    _ _ _)_ 
        (_ __ _ _)
        (_ _ _ _ _)
         (_ _ _ _)         
----._ _ _(_ _ _)           
'''

c = '''
      _ _ _ _ 
----'    _ _ _)_ _ _ _ 
               __ _ _ _)
           (_ _ _ _)
          (_ _ _ _)         
----._ _ _(_ _ _)           
'''
d = '''
      _ _ _ _ 
----'    _ _ _)_ __ _
               _ _ _ _)_
            _ _ _ ___ _ _)
              _ __ _ _ _)         
----._ _ _(_ _ _)           
'''
e = '''
      _ _ _ _ 
----'    _ _ _)_ __ _
               _ _ _ _)_ 
           _ _ __ _ _ _ _)
             _  _  _ __)         
----._ _ _ _ _ _ _ _)           
'''

# print(f"{b}\n{c}\n{a}\n{d}\n{e}")


game_image = [b, c, a, d, e]

user_input = int(input("Enter option into 0,1,2,3,4 : "))
computer_chouse = random.randrange(0, 5)

if user_input <= 4 and user_input >= 0:
    print(f"This is your chouse : \n {game_image[user_input]}")
    print(f"This is computer chouse : \n {game_image[computer_chouse]}")

if user_input > 5 or user_input < 0:
    print("Invalid chouse!")

elif user_input < computer_chouse:
    print("you lose !")

elif user_input > computer_chouse:
    print("you win!")

elif user_input == computer_chouse:
    print("match try !")

