# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:06:07 2023

@author: angie
"""

import random
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

def getRandomWord(wordDict):
    #this function returns a random string from the passed dictionary of lists of strings, and the key also.
    #first, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))
    print(wordKey)

    #second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

getRandomWord(words)

# def displayBoard(missedLetters, correctLetters, secretWord):
#     #this function displays the current state of the game board and shows the hangman figure, missed letters, and the partially revealed secret word.
#     print(HANGMAN_PICS[len(missedLetters)]) #prints the hangman figure corresponding to the number of missed letters.
#     print()

#     print('Missed letters:', end=' ') #prints 'Missed letters:' without a newline.
#     for letter in missedLetters: #prints each missed letter.
#         print(letter, end=' ')
#     print()

#     blanks = '_' * len(secretWord) #creates a string of underscore to represent the unknown letters.

#     for i in range(len(secretWord)): #replace blanks with correctly guessed letters.
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

#     for letter in blanks: #show the secret word with spaces in between each letter.
#         print(letter, end=' ')
#     print()

# def getGuess(alreadyGuessed):
#     #this function makes sure the player enters a single letter in the english alphabet and returns the letter the player enters.
#     while True:  #initiates a loop that will keep running until a valid guess is obtained from the player.
#         print('Guess a letter.') #prompts the player to guess a letter.
#         guess = input() #takes input from the player and assigns it to the variable guess.
#         guess = guess.lower() #converts valid input to lowercase so that the program handles both uppercase and lowercase letters uniformly.
#         if len(guess) != 1:  #checks if the length of the input is equal to 1
#             print('Please enter a single letter.') #if the input is not a single character, it prompts the player to enter only one letter.
#         elif guess in alreadyGuessed: #checks if the guessed letter is already present in the 'alreadyGuessed' set of letters.
#             print('You have already guessed that letter. Choose again.') #if the guessed letter has already been guessed, it informs the player and prompts for a new guess.
#         elif guess not in 'abcdefghijklmnopqrstuvwxyz':  #verifies if the input is a letter from the english alphabet.
#             print('Please enter a LETTER.') #prompts the player to enter a valid letter.
#         else:
#             return guess #if the input passes all the validation checks, the function returns the valid guessed letter to the calling code.

# def playAgain(): 
#     #this function is used to ask the player if they want to start a new game after finishing one.
#     print('Do you want to play again? (yes or no)')
#     return input().lower().startswith('y') #anything starting with 'y' is considered as a positive response to let the player play again.


# print('H A N G M A N')

# difficulty = 'X' #makes difficulty a variable X.  
# while difficulty not in 'EMH': #a while loop that runs as long as the 'difficulty' is not one of the characters in the string 'EMH' (E-Easy, M-Medium, and H-Hard).
#   print('Enter difficulty: E - Easy, M - Medium, H - Hard') #Displays a message prompting the user to input level of difficulty they wish to play the game at.
#   difficulty = input().upper() #takes the users input and changes it to uppercase and the upercase of the input is the new value of 'difficulty'.
# if difficulty == 'M':    #if the difficulty is M (Medium), it changes the HANGMAN_PICS, by deleting elements at indices 8 and 7.
#     del HANGMAN_PICS[8]
#     del HANGMAN_PICS[7]
# if difficulty == 'H':  #if the difficulty is H (Hard), it then changes the HANGMAN_PICS by deleting elements at indices 8,7,5 and 3 (removing these results in a shorter list of hangman stages making it easier to lose, therefore being harder).
#     del HANGMAN_PICS[8]
#     del HANGMAN_PICS[7]
#     del HANGMAN_PICS[5]
#     del HANGMAN_PICS[3]

# missedLetters = ''  #creates a string to store the letters guessed that are not in the word. 
# correctLetters = '' #creates a string to store the letters guessed correctly.
# secretWord, secretSet = getRandomWord(words)    #Assigns a secretWord(the word) and secretSet(the category the word is from) using a function get RandomWord(in line 53) with the words(list in line 48).
# gameIsDone = False #Initializes a variable gameIsDone as a flag to check if the game is ongoing or is finished. It is a marker to determine when to exit the main game loop. It is set to False to ensure the game loops runs and only ends when there is a break(or whether they win or lose the game.

# while True: #An infinite while loop, the loop will run until a break statement is excecuted.
#     print('The secret word is in the set: ' + secretSet) #Prints a message to the user telling them which set the secret word is apart of.
#     displayBoard(missedLetters, correctLetters, secretWord) #This uses the function displayBoard (line 63), which displays the current state of the hangman picture. It shows the picture based on the number of misguessed letters, shows the correct letters guessed as well as the missing letters still.

#     # Let the player type in a letter.
#     guess = getGuess(missedLetters + correctLetters) #This will allow the user to input a letter guess and calls the function getGuess (line 83). Ensuring the input is valid and that it hasn't been guessed previously.

#     if guess in secretWord: #If statement that checks if the letter guessed is in the secret word.
#         correctLetters = correctLetters + guess #If the letter guessed is in the secret word then it is added to the correctLetters string to indicate that the player has guessed the right letter.

#         # Check if the player has won
#         foundAllLetters = True #A flag foundAllLetters as True assuming that all the letters in the secretWord got guessed correctly.
#         for i in range(len(secretWord)): #A loop to go through each index of the secretWord string and getting a range with indices from 0 to the length of the secret word subtracting 1.
#             if secretWord[i] not in correctLetters: #If statement to check the index i of secretWord and that is not present in the correctLetters string(this means they haven't guessed the correct letter yet).
#                 foundAllLetters = False #Sets the variable foundAllLetters to False if a character in secretWord has not been guessed correctly.
#                 break #Exits the loop when a letter in secretWord hasn't been guessed correctly. 
#         if foundAllLetters: #If statement to check if all the letters in the secretWord has been found within the correctLetters string.
#             print('Yes! The secret word is "' + secretWord + '"! You have won!') #If all the letters are in the correctLetters string (foundAllLetters=True), it prints a message to the user telling them they have won the game.
#             gameIsDone = True #If all the correct letters are guessed correctly then it sets gameIsDone to True meaning the game is over and ended as a win. 
#     else: #If statement checks if the letter guessed is not in the secretWord
#         missedLetters = missedLetters + guess #If the letter guessed is not in the secretWord then the guessed letter is added to the missedLetters string. (Keeps track of all the incorect guessed letters).

#         # Check if player has guessed too many times and lost.
#         if len(missedLetters) == len(HANGMAN_PICS) - 1: #Checks if the length of the incorrectly guessed letter is equal to the length of the maximum allowed incorrect guessed(based on the the stages of the HANGMAN_PICS).
#             displayBoard(missedLetters, correctLetters, secretWord) #If the length of incorrect letters guessed is eqaul to maximum amount of guesses then calls back function displayBoard (line 63) to shown the hangman figure, the missing letters, the correctLetters guessed and the secret word. 
#             print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"') #If the user has guessed incorrectly the same as many guesses are avalible for the level of difficulty, it tells the user they had run out of guesses, and then reveals the secret word.
#             gameIsDone = True #Sets the gameIsDone flage to True which then ends the game due to running out of guesses. 

#     # Ask the player if they want to play again (but only if the game is done).
#     if gameIsDone: #If statement to check is the game is done, because they guessed the word correctly or ran our of guesses and lost the game.
#         if playAgain(): #if the game is done then it calls back to the function playAgain (line 98), asking the user if they want to play the game again. 
#             missedLetters = '' #If the users want to play again it resets the missedLetters string to be empty.
#             correctLetters = '' #The correctLetters string gets empty to get ready for a new game.
#             gameIsDone = False #gameIsDone is set to False resets the flag gameIsDone, showing that a new game is going to be ongoing. 
#             secretWord, secretSet = getRandomWord(words) #Chosses a new random secret word and it's set. 
#         else: #Checks if the user does not want to play again
#             break #If the user does not want to play again a break statement exits the loop, which stops the programming from running. 