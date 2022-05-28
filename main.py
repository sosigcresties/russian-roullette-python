import random
import time

gun = ['X', '', '', '', '', '']
soviet_counter = 0

character_list1 = ["1. Vladimir Putin", "2. Joseph Stalin", "3. Adolf Hitler"]

character_list2 = ["4. Volodymyr I forgot the surname", "5. Donald Trump", "6. pussyrub69"]

print(character_list1)
print(character_list2)
print()
char_choice = int(input("Pick a character. Type the numbers from 1-6 to pick the characters. "))

if char_choice == 1:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. Vladimir Putin wins!")
        print("Russia wins, bye bye Ukraine!")
        time.sleep(0.001)
        quit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')

if char_choice == 2:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. Joseph Stalin wins!")
        print("The F in Soviet Russia stands for Food")
        time.sleep(0.001)
        quit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')

if char_choice == 3:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. Adolf Hitler wins!")
        print("Sieg Heil! The Third Reich is always victorious!")
        time.sleep(0.001)
        quit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')

if char_choice == 4:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. Volodymyr I forgot the surname wins!")
        time.sleep(3)
        print()
        print("JK. Fuck Ukraine, You actually lose!!!")
        print("You Died...")
        exit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')

if char_choice == 5:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. Donald Trump wins!")
        print("Haha North Korean commies, you guys are getting nuked!")
        time.sleep(0.001)
        quit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')

if char_choice == 6:
  print("Character chosen.")
  print()
  while soviet_counter <= 5:
    
    spin = input("type ENTER to shoot ")
    if spin == "":
      random.shuffle(gun)
      print(gun)
    if gun[0] == '':
      print("You live.")
      print("Starting next round.")
      print()
      soviet_counter += 1
      if soviet_counter == 5:
        print("In soviet russia, you dont shoot gun. Gun shoot you.")
        print("GG. pussyrub69 wins!")
        print("Pornhub Pedo File always wins! The prize is an infinite amount of pussies to RUB!")
        time.sleep(0.001)
        quit()
    elif gun[0] == 'X':
      print("You Died...")
      exit()
    else:
        gun.remove('')