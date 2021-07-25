#creating custom exceptions
class Error(Exception):
    pass
class EmailInvalidError(Error):
    pass
ex_email='harshitha123@gmail.com'
while True:
    try:
            new_email=input('enter email')
            if(ex_email!=new_email):
                raise EmailInvalidError
            break
    except EmailInvalidError:
        print('Email Invalid....Try again')
print('Correct email')
