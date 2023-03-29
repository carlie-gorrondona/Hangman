import random

#----------------------- FUNCTIONS -----------------------#

def playGame():
    wordsArray = ["python", "javascript", "react", "ruby"]
    randomWord = random.randint(0, 3)
    gameWord = wordsArray[randomWord]
    gameDashes = ""
    userGuess = ""
    playerGuesses = 0
    wordSolved = False

    for letter in gameWord:
        if letter.isalpha() == True:
            gameDashes = gameDashes + "_ "

    while playerGuesses != 6 or wordSolved == True:
        printGallow(playerGuesses)
        gameDashes = printLettersAndDashes(gameWord, gameDashes, playerGuesses, wordSolved, userGuess)
        userGuess = playerGuess(gameWord, playerGuesses)


def printGallow(playerGuesses):

    match playerGuesses:
        case 0:
            print(" ________   ")
            print(" |      |   ")
            print(" |          ")
            print(" |          ")
            print(" |          ")
            print(" |_________ \n")            
        case 1:
            print(" ________   ")
            print(" |      |   ")
            print(" |      0   ")
            print(" |          ")
            print(" |          ")
            print(" |_________ \n")
        case 2:
            print(" ________   ")
            print(" |      |   ")
            print(" |      0   ")
            print(" |      |   ")
            print(" |          ")
            print(" |_________ \n")
        case 3:
            print(" ________   ")
            print(" |      |   ")
            print(" |    \ 0   ")
            print(" |      |   ")
            print(" |          ")
            print(" |_________ \n")
        case 4:
            print(" ________   ")
            print(" |      |   ")
            print(" |    \ 0 / ")
            print(" |      |   ")
            print(" |          ")
            print(" |_________ \n")
        case 5:
            print(" ________   ")
            print(" |      |   ")
            print(" |    \ 0 / ")
            print(" |      |   ")
            print(" |     /    ")
            print(" |_________ \n")
        case 6:
            print(" ________   ")
            print(" |      |   ")
            print(" |    \ 0 / ")
            print(" |      |   ")
            print(" |     / \  ")
            print(" |_________ \n")
        case _:
            print("Something went wrong")

def printLettersAndDashes(gameWord, gameDashes, playerGuesses, wordSolved, userGuess):

    if playerGuesses != 0 and wordSolved == False:
        for letter in gameWord:
            if userGuess == letter:
                letterIndex = gameWord.index(letter)
                print(letterIndex)
                gameDashes = gameDashes.replace(gameDashes[letterIndex], userGuess) #this is wrong at the moment
    elif playerGuesses == 0 and wordSolved == False:
        print(gameDashes)

    return gameDashes
        


            
def playerGuess(gameWord, playerGuesses):
    letterGuessedCorrectly = False
    userGuess = input("Your guess: ")

    for letter in gameWord:
        if userGuess == letter:
            letterGuessedCorrectly = True
        
    if letterGuessedCorrectly == False:
        playerGuesses += 1
        # incorrectGuesses(userGuess)
    
    return userGuess
            

# def incorrectGuesses(userGuess):
#     incorrectLetters = []
#     incorrectLetters.append(userGuess)
    
#     return incorrectLetters


    

#----------------------- MAIN -----------------------#

print("Welcome to Hangman! Select an option from the menu below.")

print("* * * * * * MENU * * * * * *")
print("*       1. Play Game       *")
print("*        2. Exit           *")
print("* * * * * * * * * * * * * * \n")

userInput = input("Your selection: ")

match userInput:
    case "1":
        playGame()
    case "2":
        print("Thanks for playing!")
    case _:
        print("Invalid input")