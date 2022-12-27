import random
import time

prize = random.choice(["a million dollars", "scammed by hacker", "one butterscotch candy", "a brand new Tesla", "nothing"])

#print pause
def print_pause(message):
    print(message)
    time.sleep(2)
#valid Input Function:
def valid_input (prompt, choice1, choice2):
    while True:
        response = input(prompt).lower()
        if response == choice1:
            return response
        elif response == choice2:
            return response
        else:
            print_pause("choice invalid. Please try again")
#main intro
def intro():
    print_pause("Welcome to this very special game to Trick or Treat!")
    print_pause("Will you be tricked or treated?")
    print_pause("I am excited to see what you will receive" )
    print_pause("Choose carefully")
    print_pause("Best of luck to you, but you must be on your way now.")

def accept_game():
    response = valid_input("Do you wish to continue?", "yes", "no")
    #accepting game play
    if response == "yes":
        print_pause("Lets begin...")
        prizes(prize)
    elif response == "no":
        print_pause("This is the chance of a lifetime. Just give it a try!")

def prizes(prize):
    print_pause( "you can win" + prize +"!")
    print_pause("will you get a trick or a treat?")
    response = valid_input("which would you like?", "treat", "trick")
    #treat function
    if response == "trick":
        print_pause("yay!")
        print_pause("lets go!")
        a_million_dollars()
    #trick function
    else:
        print_pause ("scammed by a hacker" + prize  + " prizes")
        print_pause("lets go!")
        scammed_by_a_hacker()

def a_million_dollars():
    print_pause("You have opted for yearly payments!")
    print_pause("please fill this out with you banking inforamtion")
    print_pause("lets head over to the bank.")
    print_pause( "Congratulations on your" + prize +"!")
    new_game()

def scammed_by_a_hacker():
    print_pause(" Sorry, but you have been hacked by a scammer")
    print_pause("they stole all the money from your account")
    print_pause("lets head over to the bank")
    new_game()

def new_game():
    response = valid_input("Would you like to play again?", "yes", "no")
    if response == "yes":
        print_pause("ok! Lets begin!")
        play_prizes_game()
    else:
        print_pause("See you soon! Bye for now!")

#entire game
def play_prizes_game():
    intro()
    accept_game()

play_prizes_game()