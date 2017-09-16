<<<<<<< HEAD
from send_message import send_message
from read_message import read_message
from add_status import add_status
from add_friend import add_friend
from globals import current_status_message
from  read_chat import read_chat
from termcolor import colored


def start_chat(name, age, rating, status):

    # validating users details.
    error_message = None  # variable for storing error messages.

    if not (age > 12 and age < 50):
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print colored(error_message,'red')
    else:
        welcome_message = "Authentication complete. Welcome\n" \
                          "Name : " + name + "\n" \
                          "Age: " + str(age) + "\n" \
                          "Rating: " + str(rating) + "\n" \
                          "Glad to have you on Board" + "\n"
        if rating > 4.0:
            welcome_message=welcome_message+"You are the Best"
        elif rating > 3.0:
            welcome_message=welcome_message+"Going Good but can improve further"
        else:
            welcome_message=welcome_message+"Need Lots of Efforts"
        print colored(welcome_message, 'green')

        # displaying menu for user.

    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do ? \n" \
                       "1.Add status \n" \
                       "2.Add a friend \n" \
                       "3.Send a secret message \n" \
                       "4.Read a secret message \n" \
                       "5.Read chats \n" \
                       "6.Close Application \n"

        result = int(raw_input(menu_choices))

        # validating users input
        if result == 1:
            # action
            current_status_message = add_status()
            print colored("Your Current status is: "+current_status_message, 'green')
        elif result == 2:
            # action
            no_of_friends = add_friend()
            print colored("You have %d friends " % (no_of_friends), 'green')
        elif(result ==3):
            send_message()
        elif(result ==4):
            read_message()
        elif result==5:
            read_chat()
=======
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message


# start_chat() function definition.
def start_chat(name, age, rating, status):
    from globals import current_status_message
    # validating users details.
    error_message = None # variable for storing error messages.

    if not (age > 12 and age < 50) :
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print error_message
    else:
        welcome_message = "Authentication complete. Welcome\n " \
                          "Name : " + name + "\n" \
                          "Age: " + str(age) + "\n" \
                          "Rating: " + str(rating) + "\n" \
                          "Proud to have you onboard"
        print welcome_message

    # displaying menu for user.
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n " \
                    "1. Add a status update \n " \
                    "2. Add a friend \n " \
                    "3. Send a secret message \n " \
                    "4. Read a secret message \n " \
                    "5. Read Chats from a user \n " \
                    "6. Close Application \n"
        result = int(raw_input(menu_choices))
        # validating users input
        if result == 1:
            current_status_message = add_status(current_status_message)
        elif result == 2:
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)
        elif result == 3:
            send_message()
        elif result == 4:
            read_message()
>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
        elif result == 6:
            # close application
            show_menu = False
        else:
<<<<<<< HEAD
            print colored("Wrong choice. Try again.", 'red')
=======
            print "wrong choice try again."
>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
