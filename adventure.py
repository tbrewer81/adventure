import random
import time


prizes = [
  " a million dollars",
  " being scammed by hacker",
  " one butterscotch candy",
  " a brand new Tesla",
  " ...nothing"
  ]


prize = random.choice(prizes)


g_prize = random.choice([
  " a million dollars",
  " one butterscotch candy",
  " a brand new Tesla",
  ])


b_prize = random.choice([
  " ...nothing",
  " being scammed by hacker"
  ])


# print pause
def print_pause(message, pause=0.0):
    print(message)
    time.sleep(pause)


# valid Input Function:
def valid_input(prompt, choice1, choice2):
    while True:
        response = input(prompt).lower()
        if response == choice1:
            return response
        elif response == choice2:
            return response
        else:
            print_pause("choice invalid. Please try again")


# main intro
def intro():
    print_pause("Welcome to this very special game to Trick or Treat!")
    print_pause("Will you be tricked or treated?")
    print_pause("I am excited to see what you will receive")
    print_pause("Choose carefully")
    print_pause("Best of luck to you, but you must be on your way now.")


def accept_game():
    response = valid_input("Do you wish to continue?", "yes", "no")
    if response == "yes":
        print_pause("Lets begin...")
        prizes(prize)
    elif response == "no":
        print_pause("This is the chance of a lifetime. Just give it a try!")


def prizes(prize):
    print_pause("you have a chance to win" + prize + "!")
    print_pause("will you get a trick or a treat?")
    response = valid_input("which would you like?", "treat", "trick")
    if response == 'trick':
        bad_prize()
    else:
        good_prize()


def good_prize():
    print_pause("yay!")
    print_pause("you got " + g_prize)
    print_pause("Congratulations!")


def bad_prize():
    print_pause(" Sorry, but you got " + b_prize)
    print_pause("better luck next time!")


def new_game():
    response = valid_input("Would you like to play again?", "yes", "no")
    if response == "yes":
        print_pause("ok! Lets begin!")
        global prize
        prize = random.choice([
          " a million dollars",
          " being scammed by hacker",
          " one butterscotch candy",
          " a brand new Tesla",
          " ...nothing"
          ])
        accept_game()
    else:
        print_pause("See you soon! Bye for now!")


# entire game
def play_prizes_game():
    intro()
    accept_game()
    new_game()


play_prizes_game()