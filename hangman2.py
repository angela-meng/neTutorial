# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:17:25 2023

@author: angie
"""

import random
import os

# start
print("HANGMAN")

# game data
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

# secret word parameters before guessing
wordKey = 'Colors' # pick a specific set in dictionary
secretWord = random.choice(words[wordKey]) # generate a random word in the chosen set
secretWord_list = list(secretWord)
print(secretWord)

# user begins guessing
length_secretWord = len(secretWord)
hangman_index = len(HANGMAN_PICS) - 1
print(HANGMAN_PICS[hangman_index])
i = 0
guess = input('Guess a letter: ')
# os.system('cls')

# process user's guess
continue_game = True
while continue_game == True:
    if guess in secretWord_list:
        i += 1
        print(HANGMAN_PICS[hangman_index])
        if length_secretWord != i:
            guess = input('Correct! Guess a letter: ')
        else:
            continue_game = False
    else:
        hangman_index -= 1
        if hangman_index > 0:
            print(HANGMAN_PICS[hangman_index])
            guess = input('Incorrect. Guess a letter: ')
        else:
            continue_game = False

# gives final result and ends game
if i == length_secretWord:
    print("You guessed the word.")
else:
    print(HANGMAN_PICS[hangman_index])
    print("You died.")