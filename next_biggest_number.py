#!/usr/bin/python3
import sys
from itertools import permutations 
import itertools

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    start_list = (x for x in str(num))
    perms = permutations(start_list) 
    list_of_perms = list(perms)
    num_list = (int(''.join(x)) for x in list_of_perms)
    list_of_numbers = list(num_list)
    distinct_numbers = list(set(list_of_numbers))
    greater_than = (int(x) for x in distinct_numbers if int(x) > int(num))
    greater_list = list(greater_than)
    lngth = len(greater_list)

    if lngth==0:
        min_value = -1
    else:
        min_value = min(greater_list)

    return min_value

if __name__ == "__main__":
    main()

