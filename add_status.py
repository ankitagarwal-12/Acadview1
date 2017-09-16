<<<<<<< HEAD
from termcolor import colored


STATUS_MESSAGES = ["Spy mode ON", "Busy, Call If Urgent"]
def add_status():
    tempcheck=True#temporary variable
    wholecheck=True#temporary variable
    while wholecheck:
        default = raw_input("Do you want to select from older status (y/n)? ")
        if default.upper() == "N":
            wholecheck=False
            #Setting new Status Message
            while tempcheck:
                new_status_message = raw_input("What status message do you want to set? ")
                if len(new_status_message)>0:
                    updated_status_message = new_status_message
                    STATUS_MESSAGES.append(updated_status_message)
                    tempcheck=False
                else:
                    print colored("Please enter a valid status ",'red')

        elif default.upper() == "Y":
            wholecheck=False
            while tempcheck:
                item_position = 1
                #selecting from list(Status)
                for message in STATUS_MESSAGES:
                    print str(item_position) +". "+ str(message)
                    item_position = item_position + 1
                message_selection = int(raw_input("Use Number To Select Desired Status\nEnter Choice:  "))
                if len(STATUS_MESSAGES) >= message_selection:
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    tempcheck=False
                else:
                    print colored("Select a proper status",'red')

        else:
            print colored("Wrong choice. Please try again",'red')
=======
from globals import STATUS_MESSAGES

# updated status message.
updated_status_message = None


def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input('Do you want to select from the older status (y/n)?')

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        else:
            print "You did not provided any status message. Try again."

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print 'Your updated status message is: ' + updated_status_message
        else:
            print "Invalid choice. Try again."
    else:
        print 'The option you chose is not valid! Press either y or n.'

>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
    return updated_status_message