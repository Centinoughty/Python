import random

def random_password():
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+"
    string = list(string)
    password = ""

    count = random.randrange(8, 33)

    for i in range(0, count):
        password += string[string.index(random.choice(string))]

    return password
