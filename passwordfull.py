#Lists of Usernames and Passwords
usernames = ['']
passwords = ['']

#Variables for creating an account
nuser = ''
npass = ''

#Variables for logging into an account
euser = ''
epass = ''

#Action Variable
corl = ''
action = ''

#Account creation function
def create():
    nuser = input('What will your username be?')
    npass = input('What will your password be?')
    usernames = usernames + nuser
    passwords = passwords + npass
    print('Thank you for creating an account')
    notin()

#Account login function
def login():
    #Enter username and password
    euser = input('What is your username?')
    epass = input('What is your password?')

    #Check to see if username and password match up
    if (euser == usernames[0] and epass == passwords[0]):
        print('login successful, Welcome' + euser)

    elif (euser == usernames[1] and epass == passwords[1]):
        print('login successful, Welcome' + euser)

    elif (euser == usernames[2] and epass == passwords[2]):
        print('login successful, Welcome' + euser)

    elif (euser == usernames[3] and epass == passwords[3]):
        print('login successful, Welcome' + euser)

    elif (euser == usernames[5] and epass == passwords[4]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[5] and epass == passwords[5]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[6] and epass == passwords[6]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[7] and epass == passwords[7]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[8] and epass == passwords[8]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[9] and epass == passwords[9]):
            print('login successful, Welcome' + euser)

    elif (euser == usernames[10] and epass == passwords[10]):
            print('login successful, Welcome' + euser)

#Choose to create or login
def notin():
    corl = input("Type 'create' or 'login'")
    if (corl == 'create'):
        create()

    elif (corl == 'login'):
        login()


#Call notin function
notin()
