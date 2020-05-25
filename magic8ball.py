import sys
import random
import time

while True:
    print("Hello, I'm your magic 8 ball. I can answer your question.")
    name = input('Enter your name: ')
    if name == "":
        print("You don't want my help. Fine.")
        sys.exit()
    question = input('What do you want to know? ')
    print(name,",", "you asked", "\"", question, "\"")
    time.sleep(3)
    print("What would your fortune say? Let's find out.")
    time.sleep(5)

    answers = random.randint(1, 8)

    if answers == 1:
        print ("It is certain.")
    elif answers == 2:
        print ("Outlook good.")
    elif answers == 3:
        print ("Ask again later.")
    elif answers == 4:
        print ("As I see it, yes.")
    elif answers == 5:
        print ("Reply hazy, try again.")
    elif answers == 6:
        print ("You may rely on it.")
    elif answers == 7:
        print ("Don't count on it.")
    elif answers == 8:
        print("My reply is no.")
    else:
        print("Not a valid question!")

    play_again = input("Would you like to ask another question? yes/no ").lower()
    if play_again == 'no':
        print("Goodbye. May the force be with you!")
        sys.exit()