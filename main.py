<<<<<<< HEAD
# import statements.
from spy_details import spy
from start_chat import start_chat
from globals import Spy
from termcolor import colored
import re

print "Let's get started!!!"
loop = True
while loop:
    question = "Do you want to continue as " + spy.Name + "(Y/N) ? "
    existing = raw_input(question)

    # validating users input
    if existing.upper() == "Y":
        # default user
        loop = False
        start_chat(spy.Name, spy.Age, spy.Rating, spy.SpyOnline)

    elif existing.upper() == "N":
        # new user code here
        loop = False
        check=True
        while check:
            # temporary variable
            temp = True
            # Validation Using Regular Expressions
            patternsalutation='^Mr|Ms$'
            patternname='^[A-Za-z][A-Za-z\s]+$'
            patternage='^[0-9]+$'
            patternrating='^[0-9]+\.[0-9]$'
            # Validating Each Values Using Regular Expression
            while temp:
                salutation = raw_input("Mr. or Ms.? : ")
                if (re.match(patternsalutation, salutation) != None):
                    temp = False
                else:
                    print colored("Enter Again!!!!",'red')
            temp=True
            while temp:
                spy.Name=raw_input("Enter Name: ")
                if(re.match(patternname,spy.Name)!=None):
                    temp=False
                else:
                    print colored("Enter Again!!!!",'red')
            # concatenation.
            spy.Name = salutation + "."+spy.Name
            temp=True
            while temp:
                 spy.Age = raw_input("Age?")
                 if (re.match(patternage, spy.Age) != None):
                     temp = False
                     spy.Age=int(spy.Age)
                 else:
                     print colored("Enter Again!!!!", 'red')
            temp=True
            while temp:
                spy.Rating = raw_input("Spy rating?")
                if (re.match(patternrating, spy.Rating) != None):
                    temp = False
                    spy.Rating=float(spy.Rating)
                else:
                    print colored("Enter Again!!!!",'red')
            # Checking If Spy is eligible
            if spy.Rating <= 5.0 and spy.Age > 12 and spy.Age < 50:
                start_chat(spy.Name,spy.Age,spy.Rating,spy.SpyOnline)
                check=False
            else:
                print colored("Invalid Entry!", 'red')
    else:
        print colored("Wrong choice. Try again", 'red')
=======
from spy_details import spy
from start_chat import start_chat

print "Let\'s get started"

existing = raw_input("Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): ")


if existing.upper() == "Y":
    # user wants to continue as default user.

    # concatination of salutation and name of spy.
    spy['name'] = spy['salutation'] + " " + spy['name']

    # starting chat application.
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])


elif existing.upper() == "N":
    # user wants to continue as new user
    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first:")
    # check whether spy has input something or not

    if len(spy['name']) > 0:
        print 'Welcome ' + spy['name'] + '. Glad to have you back.'
        spy['salutation'] = raw_input("What should we all you Mister or Miss? : ")
        # concatination of salutation and name of spy.
        spy['name'] = spy['salutation'] + " " + spy['name']

        print "Alright " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."

        spy['age'] = int(raw_input("Enter your age. ?"))  # converting users input to integer (typecasting)
        spy['rating'] = float(raw_input("What is your spy rating?"))  # converting users input to float (typecasting)
        spy['is_online'] = True
        if spy['rating'] > 4.5:
            print ' You are one of the Best Rated Spy'
        elif 3.5 < spy['rating'] <= 4.5:
            print 'You are a good rated Spy.'
        elif 2.5 <= spy['rating'] <= 3.5:
            print 'You are a hard Working Spy '
        else:
            print 'You Can perform better as a spy.'

        # starting chat application.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."


















>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
