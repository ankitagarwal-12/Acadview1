from spy_details import spy
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


















