'''Recursion exercise code template'''

#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def hourglass_ite(levels: int) -> None:
    # upper part
    for times in range(levels, 1, -1):
        print('{:^10}'.format('*' * (2*times-1)))
        
    # lower part
    for times in range(0, levels):
        print('{:^10}'.format('*' * (2*times+1)))

def diamond_ite(levels: int) -> None:
    # upper part
    for times in range(0, levels-1):
        print('{:^10}'.format('*' * (2*times+1)))
        
    # lower part
    for times in range(levels, 0, -1):
        print('{:^10}'.format('*' * (2*times-1)))

def hourglass_rec(levels: int) -> None:
    if levels < 1:
        pass
    else:
        if levels == 1:
            hourglass_rec(levels-2)
            print('{:^10}'.format('* ' * levels))
        else:
            print('{:^10}'.format('* ' * levels))
            hourglass_rec(levels-1)
            print('{:^10}'.format('* ' * levels))

def diamond_rec(levels: int) -> None:
    count = 1
    if count <= levels:
        diamond_rec_helper(levels, count)

def diamond_rec_helper(levels, count):
    if count <= levels:
        if levels == count:
            diamond_rec_helper(levels -1, count + 1)
            print('{:^10}'.format('* ' * count))
        else:   
            print('{:^10}'.format('* ' * count))
            diamond_rec_helper(levels, count + 1)
            print('{:^10}'.format('* ' * count))


def main():
    '''Main function'''
    hourglass_ite(5)
    hourglass_rec(5)
    diamond_ite(5)
    diamond_rec(5)


if __name__ == '__main__':
    main()
