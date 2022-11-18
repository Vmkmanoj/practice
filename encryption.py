import random
import string


char=string.ascii_letters + string.digits + string.punctuation
key=list(char)
char=key.copy()

random.shuffle(char)


plain_text=input("enter the planintext:")
normal=""
for i in plain_text:
    index=char.index(i)
    normal=normal+key[index]

print("This is your encryption",normal)


encrption_text=input("enter your encryption text:")
ena=""
for j in encrption_text:
    index=key.index(j)
    ena+=char[index]

print("This your decryptin",ena)
