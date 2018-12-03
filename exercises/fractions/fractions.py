'''
Implementation of the class Fraction
'''
#!/usr/bin/env python3


def gcd(num_a, num_b):
    '''Helper function to simplify fractions'''
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    '''Class Fraction'''
    def __init__(self, numerator: int, denominator: int) -> None:
        '''Constructor'''
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be an integer number')
        if not isinstance(denominator, int):
            raise TypeError('Denominator must be an integer number')
            # if not denominator > 0:
            #     raise Exception('Denominator must be positive')
        common = gcd(numerator, denominator)
        self.num = numerator//common
        self.denom = denominator//common

    def get_numerator(self) -> int:
        '''Return fraction numerator'''
        return self.num

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        '''Return fraction denominator'''
        return self.denom

    denominator = property(get_denominator)

    def __str__(self) -> str:
        '''Object as a string'''
        if self.num > self.denom:
            return str(self.num // self.denom) + ' ' + \
                str(self.num % self.denom) + '/' + str(self.denom)
        else:
            return str(self.num) + '/' + str(self.denom)

    def __repr__(self) -> str:
        '''Object representation'''
        return 'Fraction({}, {})'.format(self.num, self.denom)

    def __eq__(self, other: object) -> bool:
        '''Equality comparison'''
        if isinstance(other, Fraction):
            return self.num * other.denominator == other.numerator * self.denom
        else:
            raise TypeError('Can only compare Fractions')

    def __gt__(self, other: object) -> bool:
        '''Greater than comparison'''
        if isinstance(other, Fraction):
            return self.num / self.denom > other.numerator / other.denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __ge__(self, other: object) -> bool:
        '''Greater than or equal comparison'''
        if isinstance(other, Fraction):
            return self.num / self.denom >= other.numerator / other.denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __add__(self, other: object) -> object:
        '''Add two fractions'''
        new_num = self.num * other.denominator + self.denom * other.numerator
        new_denom = self.denom * other.denominator
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
        # raise NotImplementedError

    def __sub__(self, other: object) -> object:
        '''Subtract two fractions'''
        new_num = self.num * other.denominator - self.denom * other.numerator
        new_denom = self.denom * other.denominator
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
        # raise NotImplementedError

    def __mul__(self, other: object) -> object:
        '''Multiply two fractions'''
        new_num = self.num * other.numerator
        new_denom = self.denom * other.denominator
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
        # raise NotImplementedError

    def __truediv__(self, other: object) -> object:
        '''Divide two fractions'''
        new_num = self.num * other.denominator
        new_denom = self.denom * other.numerator
        
        return Fraction(new_num, new_denom)
        # raise NotImplementedError


if __name__ == "__main__":
    print("Working with Classes")
    fr_1 = Fraction(10, 4)
    print("Fraction 1 is %s" % fr_1)
    fr_2 = Fraction(10, 12)
    print("Fraction 2 is %s" % fr_2)
    fr_3 = Fraction(3, 4)
    print("Fraction 3 is %s" % fr_3)
    print("Its id is %s" % id(fr_3))
    fr_4 = Fraction(3, 4)
    print("Fraction 4 is %s" % fr_4)
    print("Its id is %s" % id(fr_4))

    print("Comparison")
    if fr_3 == fr_4:
        print("%s and %s are equal!" % (fr_3, fr_4))
    else:
        print("%s and %s are different!" % (fr_3, fr_4))

    print("%s + %s = %s" % (fr_1, fr_2, fr_1 + fr_2))