print "Let\'s get started"
spy_name = raw_input("What's your name")
if len(spy_name) > 0:
    print 'Welcome '+ spy_name + ' We are glad to have you back'
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
    spy_name = spy_salutation + " " + spy_name
    print spy_name

