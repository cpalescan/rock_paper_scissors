rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
moves = [rock, paper, scissors]

##### User

choice = int(input("Pick 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user = moves[choice]
print(moves[choice])


##### PC
import random
x = random.randint( -1 , 2)
pc = moves[x]
print(f"""Computer chose
{pc}""")

###### rules 

if user == paper and pc == rock :
  print("You  win")
elif user == scissors and pc == paper :
  print("You  win")
elif user == rock and pc == scissors :
  print("You  win")
elif moves[choice] == moves[x]:
  print("Tie")
else:
  print("You lose")