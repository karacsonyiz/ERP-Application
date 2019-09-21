import string
import random
import ui


def generate_random(table):
    generated = ''
    lowercase1 = ''.join(random.choice(string.ascii_lowercase)
                        for i in range(1))
    lowercase2 = ''.join(random.choice(string.ascii_lowercase)
                        for i in range(1))
    digit = ''.join(random.choice(string.digits) for i in range(2))
    uppercase1 = ''.join(random.choice(string.ascii_uppercase)
                        for i in range(1))
    uppercase2 = ''.join(random.choice(string.ascii_uppercase)
                        for i in range(1))  
    generated = lowercase1 + uppercase1 + digit + uppercase2 + lowercase2 + "#&"
    return generated

def get_alphabetical(list):
    n = len(list)
    for i in range(n):
        for j in range(n - 1):
            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp
    return list
