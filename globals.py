# global variables and constants here.
<<<<<<< HEAD
from termcolor import colored
from steganography.steganography import Steganography
=======
>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39

# current status message is initialized to None.
current_status_message = None

# list to store status messages.
<<<<<<< HEAD
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

# lists to store users friends information.
friends = []


# Spy Class
class Spy:
    def __init__(self, salutation, name, age, rating, isonline):
        # Assigning Values
        self.Name = salutation+"."+name
        self.Age = age
        self.Rating = rating
        self.SpyOnline = isonline
        self.chat = []

    def displayDetails(self):
        print self.Name, " ", self.Age

    def calcAverageWords(self):
        # Average Words Spoken
        avg = 0
        if len(self.chat)!=0:
            for i in self.chat:
                avg=avg+len(Steganography.decode(i.Message))
            avg=avg/(len(self.chat))
        print "Average Words Spoken: ", avg


# Chat class
class Chat:
    def __init__(self, msgImage, timestamp):
        # Assigning Values
        self.Message=msgImage
        self.Timestamp=timestamp

    def displayMessage(self):
        print colored(self.Timestamp, 'blue'), "\nMessage: ", self.Message, "\n"
=======
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

# lists to store users friends information.
friends = []
>>>>>>> b1d7c28834c2a45816b8c25815d734dfcaef3f39
