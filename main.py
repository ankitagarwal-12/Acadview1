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
