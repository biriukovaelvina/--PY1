import random
import string


from random import sample
def get_random_password() -> str:
    symbols = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
    password = ''
    d = random.sample(symbols, 8)
    password += "".join(d)
    return password
print(get_random_password())
