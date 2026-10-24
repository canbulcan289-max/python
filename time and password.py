import time
import random
import string
mistake=0
def letter_choicer():
    global letterlist
    global mistake
    alphabet=list(string.ascii_lowercase)
    letterlist=[]
    try:
        letter_number=int(input("How many letters do you want for create the password:"))
        letterlist=random.choices(alphabet,k=letter_number)
    except Exception:
        print("You have to enter an integer.")
        mistake=1
def number_choicer():
    global numberlist
    global mistake
    strnumber=string.digits
    numberlist=[]
    try:
        number_range=int(input("How many digits do you want for create the password:"))
        numberlist=random.choices(strnumber,k=number_range)
    except Exception:
        print("You have to enter an integer.")
        mistake=1
def password_creator():
    global letterlist
    global numberlist
    global real_password
    pre_password=numberlist+letterlist
    random.shuffle(pre_password)
    real_password="".join(pre_password)
    print(real_password)
letter_choicer()
number_choicer()
if(mistake==0):
    start=time.perf_counter()
    password_creator()
end=time.perf_counter()
local_time=time.localtime()
date=time.strftime("Date = %d.%m.%Y | Time = %H.%M.%S",local_time)
if(mistake==1 or not real_password):
    print("Password couldn't generated.")
else:
    print(date)
    print(f"Password generated in {end - start:.8f} seconds.")
    with open("sifre_liste.txt","a",encoding="utf-8") as file:
        file.write("Your password: "+real_password+" Generated in: "+date+"\n")
