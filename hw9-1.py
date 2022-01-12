# Author: CMOB 1/10/2022

def even_occur(lst):
    lst1 = []
    for index, value in enumerate(lst):
        if index % 2 == 0:
            lst1.append(value);
    return lst1
        

print(even_occur([2,4,5,7,3,2,24,5,6]))
