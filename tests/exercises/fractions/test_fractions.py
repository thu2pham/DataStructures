'''
Testing the class Fraction
Roman Yasinovskyy, 2017
'''
#!/usr/bin/python3


import pytest
from exercises.fractions.fractions import Fraction


class TestFractionMethods:
    '''Testing class Fraction'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.fraction1 = Fraction(1, 3)
        self.fraction2 = Fraction(4, 6)
        self.fraction3 = Fraction(6, 4)

    def test_init(self):
        '''Testing init'''
        assert self.fraction1 == Fraction(1, 3)

    def test_init_simplification(self):
        '''Testing init with gcd'''
        assert self.fraction2 == Fraction(2, 3)

    def test_init_numerator_error(self):
        '''Testing numerator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1.5, 2)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Numerator must be an integer number'

    def test_init_denominator_error(self):
        '''Testing denominator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 2.5)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Denominator must be an integer number'

    def test_init_numerator_error_2(self):
        '''Testing numerator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction('1', 2)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Numerator must be an integer number'

    def test_init_denominator_error_2(self):
        '''Testing denominator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, '2')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Denominator must be an integer number'

    def test_get_numerator(self):
        '''Testing numerator getter'''
        assert self.fraction1.get_numerator() == 1

    def test_get_numerator_2(self):
        '''Testing numerator getter'''
        assert self.fraction1.numerator == 1

    def test_get_denominator(self):
        '''Testing denominator getter'''
        assert self.fraction1.get_denominator() == 3

    def test_get_denominator_2(self):
        '''Testing denominator getter'''
        assert self.fraction1.denominator == 3

    def test_str(self, capsys):
        '''Testing __str__method'''
        print(self.fraction3)
        out, err = capsys.readouterr()
        assert out.strip() == '1 1/2'

    def test_repr(self, capsys):
        '''Testing __repr__method'''
        print(repr(self.fraction3))
        out, err = capsys.readouterr()
        assert out.strip() == 'Fraction(3, 2)'

    def test_eq(self):
        '''Testing equality operator'''
        assert Fraction(1, 3) == Fraction(2, 6)

    def test_eq_error(self):
        '''Testing equality operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) == 1
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only compare Fractions'

    def test_gt(self):
        '''Testing greater-than operator'''
        assert Fraction(1, 3) > Fraction(1, 4)
        assert Fraction(1, 2) < Fraction(2, 3)

    def test_gt_error(self):
        '''Testing greater-than operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) > 1
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only compare Fractions'

    def test_ge(self):
        '''Testing greater-than-or-equal operator'''
        assert Fraction(1, 3) >= Fraction(1, 4)
        assert Fraction(1, 2) <= Fraction(2, 3)

    def test_ge_error(self):
        '''Testing greater-than-or-equal operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) >= 1
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only compare Fractions'

    def test_add(self):
        '''Testing addition operator'''
        assert (self.fraction1 + self.fraction2) == Fraction(1, 1)

    def test_add_error(self):
        '''Testing addition operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) + '1'
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only add two Fractions'

    def test_sub(self):
        '''Testing subtraction operator'''
        assert (self.fraction1 - self.fraction2) == Fraction(-1, 3)

    def test_sub_error(self):
        '''Testing subtraction operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) - '1'
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only subtract two Fractions'

    def test_mult(self):
        '''Testing multiplication operator'''
        assert (self.fraction1 * self.fraction2) == Fraction(2, 9)

    def test_mult_error(self):
        '''Testing multiplication operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) * '1'
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only multiply two Fractions'

    def test_truediv(self):
        '''Testing true division operator'''
        assert (self.fraction1 / self.fraction2) == Fraction(1, 2)

    def test_truediv_error(self):
        '''Testing true division operator error'''
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 3) / '1'
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can only divide two Fractions'


if __name__ == '__main__':
    pytest.main(['test_fraction.py'])