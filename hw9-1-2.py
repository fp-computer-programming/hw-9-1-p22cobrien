# Author: CMOB 1/12/2022

def odd_num(lst):
    lst1 = []
    try:
        for index, value in enumerate(lst):
            if value % 2 != 0:
                print(index, value);
        return lst1
    except:
        print("numbers only")
        

print(odd_num([2,4,5,7,3,2,24,5,6]))
