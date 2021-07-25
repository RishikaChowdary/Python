import string
import random

s1 = string.ascii_letters
s2=string.digits
s3=string.punctuation
s=list(s1+s2+s3)
random.shuffle(s)
length=input("Enter length of your password(greater than or equal to 8 characters)")
while not length.isnumeric():
   length= input("Your password length must be between 7 and 64. \nPlease Re-enter")
length=int(length)
while length<8 or length>64:
    length = input("Your password length must be between 7 and 64. \nPlease Re-enter ")
    while not length.isnumeric():
        length = input("Your password must be a number. \nPlease Re-enter")
    length = int(length)
else:
    password="".join(s[:length])
    print("Generated password is:",password)