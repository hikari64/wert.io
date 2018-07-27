import random as r
import string
def id():
    	number = 1999999999
    	i = 1000000000
    	if i in range(number):
        	number = r.randint(i,number)
        	return number
def random_string_generator(size=40, chars=string.ascii_lowercase + string.digits):
    return ''.join(r.choice(chars) for _ in range(size))