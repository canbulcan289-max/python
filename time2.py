import time
import random
import string
from itertools import permutations
def letter_choicer():
    global united_letters
    letterlist=[]
    try:
        letter_number=int(input("How many letter do you want for create the password:"))
    except Exception:
        print("You have to enter an integer.")
    alphabet=list(string.ascii_lowercase)
    letterlist=random.choices(alphabet,k=letter_number)
    united_letters="".join(letterlist)
def number_choicer():
    global united_numbers
    numberlist=[]
    try:
        number_range=int(input("How many number do you want for create the password:"))
    except Exception:
        print("You have to enter an integer."),
    numberlist=random.choices(range(9),k=number_range)
    united_numbers="".join(numberlist)
def password_creator():
    global united_letters
    global united_numbers
    pre_password=united_numbers+united_letters
    real_password=permutations(pre_password)
    print(real_password)

