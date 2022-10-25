import random
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
no = "1234567890"
Symbl = '''~`!@#$%^&*()_-+={}[]:"">?<,./'';'''
all = Upper + lower + no + Symbl
Length = 8
password="".join(random.sample(all,Length))    # .join is important to use as it will replace (,) or list view 

print(f" Password Generated : {password}")
