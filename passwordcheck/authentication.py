from getpass import getpass
def authenticate(database):
    user=input('Enter user name: ')
    if database.get(user) is not None:
        password = getpass('Enter password : ')
        while password!=database.get(user):
            password = getpass('Enter password again: ')
        print('Verified')
    else:
        print('Username not exist')
database={'manoj':'1234567','konda':'12345789'}
authenticate(database)
