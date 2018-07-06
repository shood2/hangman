from random import randint

print("Welcome to Hangman!!")

words = ["rhythm", "penguin", "apple", "computer", "data", "variable", "list", "loop"]
wordChoice = randint(0, len(words))

chosenWord = list(words[wordChoice])
displayedWord = ""

for i in range(0, len(chosenWord)):
    displayedWord += "-"

display = list(displayedWord)
incorrectGuesses = list("")

playGame = True
while(playGame == True):
    if(not("-" in display)):
        playGame = False
        print("Congrats! You've won!")
    elif(len(incorrectGuesses) >= 5):
        playGame = False
        print("Sorry, you've lost...")
        print("    O   ")
        print("   \|/  ")
        print("    |   ")
        print("   / \  ")
    else:
        print("You have guessed %d incorrect letters" %(len(incorrectGuesses)))
        print("You've guessed %s" %(",".join(incorrectGuesses)))
        print("".join(display))
        inputString = input("Please make a guess:  ")
        if(inputString.isalpha() and inputString.lower() == words[wordChoice]):
            playGame = False
            print("That was correct, congratulations, you've won!")
        elif(len(inputString) > 1):
            while(len(inputString) > 1):
                inputString = input("You must input a character or guess the word correctly")
        elif(inputString.isalpha() and inputString.lower() in incorrectGuesses):
            print("You've already guessed that!")
        elif(inputString.isalpha() and inputString.lower() in chosenWord):
            for i in range(0, len(chosenWord)):
                if(inputString.lower() == chosenWord[i]):
                    display[i] = inputString
        else:
            print("Oops, that's not in the word")
            incorrectGuesses.append(inputString)
