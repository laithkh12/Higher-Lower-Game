# TODO : Display art
from art import logo, vs
from game_data import data
import random

def formatData(account):
    """
    Takes the account data and return the printable format
    :param account:
    :return:
    account data
    """
    accountName = account["name"]
    accountDescr = account["description"]
    accountCountry = account["country"]
    return f"{accountName}, a {accountDescr}, from {accountCountry}"

def checkAnswer(userGuess, aFollowers, bFollowers):
    """
    Take a user guess and follower counts and returns if they got it right.
    :param userGuess:
    :param aFollowers:
    :param bFollowers:
    :return:
    if they got it right
    """
    if aFollowers > bFollowers:
        return userGuess == "a"
    else:
        return userGuess == "b"


print(logo)
score = 0
gameShouldContinue = True
accountB = random.choice(data)

# TODO : Make sure game repeatable

while gameShouldContinue:
    # TODO : Generate a random account from the game_data

    # TODO : Making account at position B become the next account at position A
    accountA = accountB
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {formatData(accountA)}.")
    print(vs)
    print(f"Against B: {formatData(accountB)}.")

    # TODO : Ask user for a guess
    guess = input("Who has more followers? 'A' or 'B': ").lower()

    # TODO : Clear screen
    print("\n" * 20)
    print(logo)

    # TODO : Check if user is correct
    #   1. Get follower count of each account
    aFollowerAccount = accountA["follower_count"]
    bFollowerAccount = accountB["follower_count"]

    #   2. Use if statement to check if user is correct
    # TODO : Give user feedback on their guess
    # TODO : Score keeping
    isCorrect = checkAnswer(guess, aFollowerAccount, bFollowerAccount)
    if isCorrect:
        score += 1
        print(f"Correct!. Current score {score}")
    else:
        print(f"Incorrect. Final score {score}")
        gameShouldContinue = False



