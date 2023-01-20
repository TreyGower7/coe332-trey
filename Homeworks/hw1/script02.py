
import names 
x=0
while x != 5:
    name = names.get_full_name()
    if len(name) == 9:
        print(name)
        x = x+1
