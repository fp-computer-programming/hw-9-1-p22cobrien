# Author: CMOB 1/12/2022

def find_thing(lst, item):
    try:
        for index, value in enumerate(lst):
            if value == item:
                find = index
                break

    finally:
        try:
            if find == index:
                print(find)
        except UnboundLocalError:
            print(-1)


find_thing("traceback", "k")
find_thing(["pie",1800,"how about no",2,4,"perhaps"], 2)
