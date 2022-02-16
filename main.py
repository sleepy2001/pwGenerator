import random
import string

print('Hello, welcome to Random Password Generator')

length=int(input('Please input the length of the desired password: '))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower+upper+num+symbols

temp=random.sample(all,length)

password="".join(temp)

print(password)