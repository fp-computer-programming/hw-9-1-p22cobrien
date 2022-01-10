# Author: CMOB 1/10/2022

def someting(lst):
    for index, value in enumerate(lst):
        if index % 2 == 0:
            return value
        else:
            continue
        

print(someting([2,4,5,7]))
