stage = 0

def find_stage (stage_number):
  if stage_number == 0:
    print (stage0)
  if stage_number == 1:
    print (stage1)
  if stage_number == 2:
    print (stage2)
  if stage_number == 3:
    print (stage3)
  if stage_number == 4:
    print (stage4)
  if stage_number == 5:
    print (stage5)
  if stage_number == 6:
    print (stage6)



stage0 = '''

      _________
     |         |
               |
               |
               |
     __________|
'''

stage1 = '''

      _________
     |         |
     O         |
               |
               |
     __________|
'''

stage2 = '''

      _________
     |         |
     O         |
     |         |
               |
     __________|
'''

stage3 = '''

      _________
     |         |
     O         |
    /|         |
               |
     __________|
'''

stage4 = '''

      _________
     |         |
     O         |
    /|\        |
               |
     __________|
'''

stage5 = '''

      _________
     |         |
     O         |
    /|\        |
    /          |
     __________|
'''

stage6 = '''

       _________
      |         |
      O         |
     /|\        |
     / \        |
      __________|
'''

import time
import random
from random import shuffle
all_words = [['proxy1'], ['proxy2'],['proxy3'] ,['one', 'cat', 'dog', 'net', 'bed', 'car', 'fox', 'kid', 'man', 'rag', 'art', 'wig'],['goat', 'shoe', 'love', 'hand', 'bean', 'bike', 'chef', 'coin', 'edgy', 'mask'],['cream', 'short', 'piano', 'fruit', 'juicy', 'water', 'metal', 'theif', 'thick', 'anime'],['sticker' , 'window' , 'forest' , 'tuxedo' , 'tongue' , 'weapon' , 'wizard'],['picture', 'blanket', 'monster' , 'dolphin', 'diamond', 'shotgun'],['keyboard', 'triangle', 'computer',  'laughter'],['moustache', 'chemistry', 'boulevard', 'nightmare', 'abduction', 'signature', 'snowflake'],['trampoline', 'tambourine', 'background', 'binoculars','exhaustion', 'hypnotized']]


print("")
print('This is Hangman. You get 6 chances to guess the word before I am hung.')
time.sleep(1)

def random_word(letters):
  new = all_words[int(letters)]
  shuffle(new)
  word = new[0]
  return (word)


startup = 0
while startup == 0:
  print("")
  number_of_letters = input ('How many letters do you want in your word? (between 3 and 10)\n')
  try:
    if int(number_of_letters) > 2 and int(number_of_letters) < 11:
     random_word(int(number_of_letters))
     break
  except:
    print("You can only choose 3-10 letter words.")

word = random_word(number_of_letters)
right = False


# Here is the actual code for guessing:

number_correct = 0
guessed_letters = []
guesses = 6
print(stage0)
print ('_ \n' * len(word))
while guesses > 0:
  print("")
  guess = input("What letter will you guess?\n")
  guess = guess[0]
  if guess == " ":
    print("That's not a letter. Try again.")
  elif guess not in guessed_letters:
    for char in word:
      if guess == char:
        if word.find(guess) == 0:
          ending = "st"
        elif word.find(guess) == 1:
          ending = "nd"
        elif word.find(guess) == 2:
          ending = "rd"
        elif word.find(guess) >= 3:
          ending = "th"
        print ('You guessed it! "'+ guess + '" is the '+ str(word.find(guess) + 1) + '%s letter.'% ending)
        right = True
        find_stage(stage)
    if right == False:
      guesses -= 1
      print("")
      print("Incorrect. You still have %s guesses."% guesses)
      stage += 1
      find_stage(stage)
    right = False
    guessed_letters.append(guess)
  else:
    print('You already guessed that!')
  for letter in word:
    if letter in guessed_letters:
      number_correct += 1
      if number_correct == len(word):
        for char in word:
           if char in guessed_letters:
             print(char)
           else:
             print("_ ")
        time.sleep(0.5)
        print("""
        """)
        print('The word was "%s". You guessed it, so you win!'%word)
        exit()
    else:
      number_correct = 0
  print("")
  for char in word:
    if char in guessed_letters:
      print(char)
    else:
      print("_")

print("")
print('You lose! Too bad :(')
print('The word was "%s".'%word)
exit()
