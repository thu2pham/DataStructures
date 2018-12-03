'''Banking classes implementation'''
#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Address:
    '''Address class'''
    def __init__(self, street_init: str, city_init: str, state_init: str, zip_init: str):
        '''__init__'''
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    # TODO: Implement data members as properties
    @property
    def street(self):
        return self._street
    @street.setter
    def street_init(self, new_value):
        self._street = new_value
    
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, new_value):
        self._city = new_value
    
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, new_value):
        self._state = new_value
    
    @property
    def zip(self):
        return self._zip
    @zip.setter
    def zip(self, new_value):
        self._zip = new_value
    
    def __eq__(self, other: object):
        '''Compare 2 addresses'''
        if self._street == other._street and self._city == other._city and self._state == other._state and self._zip == other._zip:
            return True
        else:
            return False


    def __str__(self):
        '''__str method'''
        return "{}\n{}, {} {}".format(self._street, self._city, self._state, self._zip)

class Customer():
    '''Customer class'''
    def __init__(self, name_init: str, dob_init: str, address_init: object):
        '''Constructor'''
        self._address = address_init
        self._name = name_init
        self._dob = dob_init

    # TODO: Implement data members as properties
    @property
    def name(self):
        return self._name
    @name.setter
    def zip(self, new_value):
        self._name = new_value
    
    @property
    def dob(self):
        return self._dob
    @dob.setter
    def dob(self, new_value):
        self._dob = new_value

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, new_value):
        self._address = new_value

    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address

        return "{}".format(self._address)

    def __str__(self):
        '''__str'''
        return "{} ({})\n{}".format(self._name, self._dob, self._address)


class Account(ABC):
    '''Account class'''
    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._balance = balance_init

    # TODO: Implement data members as properties
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, new_value):
        self._owner = new_value
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, new_value):
        self._balance = new_value

    def deposit(self, amount: float):
        '''Add money'''
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            raise ValueError('Must deposit positive amount')

    def close(self):
        '''Close account'''
        self._balance = 0
        
    def __str__(self):
        '''__str__'''
        return "Owner: {}\nBalance: {:.2f}".format(self._owner, self._balance)

class CheckingAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, fee_init: float, balance_init: float=0):
        '''Constructor'''
        super().__init__(owner_init, balance_init)
        self._fee = fee_init

    def process_check(self, amount: float):
        '''Process a check'''
        if self._balance < amount:
            self._balance = self._balance - self._fee
        else:
            self._balance = self._balance - amount
        return self._balance
        
    def __str__(self):
        '''__str__'''
        return "Checking account\n" + super().__str__()


class SavingsAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, interest_rate_init: float, balance_init: float=0):
        '''Constructor'''
        super().__init__(owner_init, balance_init)
        self._interest_rate = interest_rate_init        

    def yield_interest(self):
        '''Yield annual interest'''
        self._interest_rate= self._balance * self._interest_rate/100
        self._balance = self._balance + self._interest_rate
        return self._interest_rate

    def __str__(self):
        '''__str__'''
        return "Savings account\n" + super().__str__()
        
