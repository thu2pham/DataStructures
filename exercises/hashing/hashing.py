'''Hashing exercise code template'''

#!/usr/bin/env python3

import random


def hash_remainder(key: int, size: int):
    '''Find hash using remainder'''
    return key%size

def hash_mid_sqr(key, size):
    '''Find hash using mid-square method'''
    squared = key**2
    digit = [int(d) for d in str(squared)]
    # print(digit)
    middle = float(len(digit)) / 2
    if middle % 2 != 0:
        digit.insert(0, 0)
        middle = float(len(digit)) / 2
        mid_num1 = digit[int(middle - 1)]
        mid_num2 = digit[int(middle)]
    else:
        mid_num1 = digit[int(middle - 1)]
        mid_num2 = digit[int(middle)]
            
    two_mid = int(str(mid_num1) + str(mid_num2))
    # print(two_mid)    
    i = two_mid % size

    
    return i


def hash_folding(key: str, size: int):
    '''Find hash using folding method'''
    new_str = key.replace('-','')
    num_list = []
    for num in new_str:
        num_list.append(num)
  
    hash_val = 0
    for position in range(len(new_str)):
        try:
            str1 = str(num_list[0])
            str2 = str(num_list[1])
            str_concat = str1 + str2
    
            fold = int(str_concat)
            hash_val += fold
            num_list.pop(0)
            num_list.pop(0)
        except IndexError:
            pass

    return hash_val%size

def hash_str(key: str, size: int):
    '''Find string hash using simple sum-of-values method'''
    str_sum = 0
    for position in range(len(key)):
        str_sum = str_sum + ord(key[position])
    return str_sum % size

def hash_str_weighted(key: str, size: int):
    '''Find string hash using character positions as weights'''
    str_sum = 0
    for position in range(len(key)):
        str_sum = str_sum + (ord(key[position]) * position)
    return str_sum % size


def main():
    '''Main function'''
    keys_int = [10, 21, 32, 18, 17, 19, 42, 23, 99]
    keys_int_2 = [54, 26, 93, 17, 77, 31]
    keys_intstr = ['563-555-1234', '800-555-8080', '888-555-0000']
    keys_intstr_2 = ['436-555-4601']
    keys_str = ['pavel', 'bruce', 'talia', 'harvey', 'jim', 'alfred', 'lucius', 'jonathan', 'bane']
    keys_str_2 = ['algorithm', 'logarithm']

    print('Simple remainder')
    print([hash_remainder(x, 16) for x in keys_int])
    print([hash_remainder(x, 11) for x in keys_int_2])

    print('Mid-square')
    print([hash_mid_sqr(x, 16) for x in keys_int])
    print([hash_mid_sqr(x, 11) for x in keys_int_2])

    print('Folding')
    print([hash_folding(x, 16) for x in keys_intstr])
    print([hash_folding(x, 11) for x in keys_intstr_2])

    print('String hashing')
    print([hash_str(x, 16) for x in keys_str])
    print([hash_str(x, 11) for x in keys_str_2])

    print('Weighted string hashing')
    print([hash_str_weighted(x, 16) for x in keys_str])
    print([hash_str_weighted(x, 11) for x in keys_str_2])


if __name__ == '__main__':
    main()
