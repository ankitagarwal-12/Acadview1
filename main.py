from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online
print "Let\'s get started"

existing = raw_input("Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? ")

def start_chat(spy_name,spy_age, spy_rating):

    print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
        spy_rating) + " Proud to have you onboard"


if existing == "Y":
    start_chat(spy_name,spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False


    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:

        print 'Welcome ' + spy_name + '. Glad to have you back.'
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")
        spy_name = spy_salutation + " " + spy_name

        print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

        spy_age = int(raw_input("What is your age?"))
        if 12 < spy_age < 50:
            spy_rating = float(raw_input("What is your spy rating?"))

            if spy_rating > 4.5:
                print ' You are one of the Best Rated Spy'
            elif 3.5 < spy_rating <= 4.5:
             print 'Good rated Spy.'
            elif  2.5 <= spy_rating <= 3.5:
                print 'Hard Working Spy '
            else:
                print 'Can perform better.'

            spy_is_online = True

            start_chat(spy_name, spy_age, spy_rating)


        else:
            print 'Sorry you are not eligible to be a spy'

    else:
        print "A spy needs to have a valid name. Try again please."