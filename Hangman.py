
import sys      
import random   
import string   
import math
from os import system, name

#Graphics generation
def graphics(lives, difficulty):

    graph_0 ="""
        +---+
            |
            |
            |
            |
            |
        ========="""

    graph_1 ="""
        +---+
        |   |
            |
            |
            |
            |
        ========="""

    graph_2 = """
        +---+
        |   |
        O   |
            |
            |
            |
        ========="""

    graph_3 ="""
        +---+
        |   |
        O   |
        |   |
            |
            |
        ========="""

    graph_4 ="""  
        +---+
        |   |
        O   |
       /|   |
            |
            |
        ========="""
    graph_5 ="""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        ========="""    
    graph_6 ="""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        ========="""
    graph_7 ="""
        GAME OVER
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========= """         

    if difficulty == 1:
        if lives == 7:
            print(graph_0)
        elif lives == 6:
            print(graph_1)
        elif lives == 5:
            print(graph_2)
        elif lives == 4:
            print(graph_3)
        elif lives == 3:
            print(graph_4)
        elif lives == 2:
            print(graph_5)
        elif lives == 1:
            print(graph_6)
        elif lives == 0:
            print(graph_7)    

    elif difficulty == 2:
        if lives == 5:
            print(graph_0)
        elif lives == 4:
            print(graph_2)
        elif lives == 3:
            print(graph_3)
        elif lives == 2:
            print(graph_5)
        elif lives == 1:
            print(graph_6)
        elif lives == 0:
            print(graph_7)

    elif difficulty == 3:
        if lives == 3:
            print(graph_0)
        elif lives == 2:
            print(graph_3)
        elif lives == 1:
            print(graph_5)
        elif lives == 0:
            print(graph_7)

    elif difficulty == 4:
        if lives == 1:
            print(graph_0)
        elif lives == 0:
            print(graph_7)


#Random word selection from file
def word_select(difficulty):

    document = open("countries-and-capitals.txt", "r" )
    L = list(document.readlines())
    if difficulty == 1: 
        new_list = L[0:int(math.floor(len(L)/4))]
    elif difficulty == 2: 
        new_list = L[0:int(math.floor(len(L)/2))]
    elif difficulty == 3:
        new_list = L[0:int(math.floor(len(L)*3/4))]
    elif difficulty == 4:
        new_list = L 
    
    random_line = random.choice(new_list)

    word = (random_line.split(" -"))[0]
    return word
    
    document.close()


#Difficulty level selection
def level():
    while True:
        level = input("Please select the difficulty level (Easy, Medium, Hard, Impossible) or 'quit' if you'd like to exit the game: ")
        if level == "quit":
                sys.exit(0)

        if level.lower() == "easy":
            lives = 7
            difficulty = 1
            return lives, difficulty
        elif level.lower() == "medium":
            lives = 5
            difficulty = 2
            return lives, difficulty
        elif level.lower() == "hard":
            lives = 3
            difficulty = 3
            return lives, difficulty 
        elif level.lower() == "impossible":
            lives = 1
            difficulty = 4
            return lives, difficulty
        else: 
            print("Please select a valid difficulty level!")


def clear():
    if name == 'nt':
        _ = system('cls')


#Victory screen
def victory_screen(word):
    print("Congratulations! You have won!\nYour word is " + word + "\n" )
    print("""

    ██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
    ██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
    ╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
    ░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
    ░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
    ░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
    """)


#Hangman gameplay
def play(word, lives, difficulty):
    # print(word) #Cheat
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    dashes = list(len(word) * "_")

    if " " in word:
        for i in range(0, len(word)):
            if word[i] == " ":
                dashes[i] = " "

    print("Your current word to guess: " + "|| " + " ".join(dashes) + " ||")
    print("Number of remaining tries: " + str(lives))

    while lives > 0:
        while True:

            letter = input("Please insert any unused letter or 'quit' if you want to exit the game: ")
            if letter == "quit":
                sys.exit(0)
            elif letter.lower() in alphabet:
                alphabet.remove(letter.lower())
                used_letters.add(letter.lower())
                break
            elif letter.lower() in used_letters:
                print("This letter has already been used! Please select another letter! ")
                print("You have already used: " + str(used_letters))
            else:
                print("Please select an unused letter!")
                print("You have already used: " + str(used_letters))

        if letter.lower() in word.lower():
            for i in range(0, len(word)):
                if word[i].lower() == letter.lower():
                    dashes[i] = word[i]
        else:
            lives -= 1
            print("WRONG LETTER! You've lost your life! You have " + str(lives) + " left!")            
            print("You have already used: " + str(used_letters))
        clear()
        graphics(lives, difficulty) 

        if "_" in dashes:
            print("Your current word to guess: " + "|| " + " ".join(dashes) + " ||")
        else:
            victory_screen(word)
            break

    if lives == 0:
        print("You have lost all of your lives! The game has ended!")
        graphics(lives, difficulty)


#Hangman callout
def hangman():
    clear()
    print("Hello o/! Let's play a game! ")
    
    lives, difficulty = level()
    clear()

    word = word_select(difficulty)
    clear()
    
    play(word, lives, difficulty)

    print("Goodbye! ")

hangman()