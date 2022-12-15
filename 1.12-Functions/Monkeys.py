import random
import string
# function that generates random string of 28 chars

def generateString():
    # gen string
    return(''.join(random.choices(string.ascii_lowercase, k = 28)))
