#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == -1:
        return None
    elif idx > my_list:
        return None
    print("Elements at index {:d} is {}".format(idx, element_at(my_list, idx)))
