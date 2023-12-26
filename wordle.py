import random
import sys

def main():
    answer = getRandomWord()
    attempts= 0
    for attempt in range(6, 0, -1):
        guess= input("Enter a 5 letter guess?")
        attempts += 1
        print()
        if guess.lower()==answer:
            printGuessColors(guess, answer)
            print(f"You Won! That took {attempts} guess(es).")
            break
        else:
            printGuessColors(guess, answer)
    else:
        print(f"You lost. The answer was {answer}.")

#helper to print guess with color to console
def printGuessColors(guess, answer):
    for i in range(len(guess)):
        color= letterColor(i, guess, answer)
        print(f"{guess[i]} - {color}")

#helper to determine color
def letterColor(index, guess, answer):
    if guess[index]== answer[index]:
        return "Green"
    elif guess[index] in answer:
        return "Yellow"
    else:
        return "Red"

#retrieves random word from file
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]
        file.close()
        return random.choice(words)

if __name__ == "__main__":
    main()
