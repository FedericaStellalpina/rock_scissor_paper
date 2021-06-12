#Review the variables passed
#Is it possible to simplify?

from random import choice
import sys
#I don't like having to use sys to exit the program, but how can I do it without?
#new test comment

tools = ['scissor', 'paper', 'rock']

def intro():
    print("Let's play some good, old Rock, Scissor, Paper!")
    user_score = 0
    machine_score = 0
    begin(user_score, machine_score)


def begin(user_score, machine_score):
    print()
    user_input = input('Choose: Rock, Scissor or Paper? ').lower()
    print()
    if user_input == 'scissor' or user_input == 'paper' or user_input == 'rock':
        machine_input=choice(tools)
        print("Computer's choice: ", machine_input)
        game(user_input, machine_input, user_score, machine_score)
    else:
        print('No cheating! You can only input Rock, Scissor or Paper. Try again, please.')
        begin(user_score, machine_score)

def game(user_input, machine_input, user_score, machine_score):
    
    if user_input == 'rock' and machine_input == 'scissor':
        win = True
        victory(win, user_score, machine_score)
    elif user_input == 'paper' and machine_input == 'rock':
        win = True
        victory(win, user_score, machine_score)
    elif user_input == 'scissor' and machine_input == 'paper':
        win = True
        victory(win, user_score, machine_score)
    elif user_input == machine_input:
        print("It's a tie, try again")
        begin(user_score, machine_score)
    else:
        win = False
        victory(win, user_score, machine_score)

def victory(win, user_score, machine_score):
    while user_score != 3 and machine_score != 3:
        if win == True:
            print()
            print ('Your point!')
            print()
            user_score += 1
            print ('Your score: ', user_score)
            print ("Computer's score: ", machine_score)
            if user_score == 3 or machine_score ==3:
                the_winner(user_score, machine_score)
            else:
                begin(user_score, machine_score)
            
        else:
            print()
            print ("Computer's point!")
            print()
            machine_score +=1
            print ('Your score: ', user_score)
            print ("Computer's score: ", machine_score)
            if user_score == 3 or machine_score ==3:
                the_winner(user_score, machine_score)
            else:
                begin(user_score, machine_score)


def the_winner(user_score, machine_score):
    if user_score == 3:
        print()
        print('You are the winner!')
        print()
        rematch()
    elif machine_score == 3:
        print()
        print('The computer wins!')
        print()
        rematch()

def rematch():
    try_again = input('Would you like to try again? ').lower()
    if try_again == 'yes':
        intro()
    elif try_again == 'no':
        print('Thank you, goodbye!')
        sys.exit()
    else:
        print('Please input yes, or no')
        rematch()
intro()
