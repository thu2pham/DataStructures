'''Reverse Polish Notation'''

#!/usr/bin/env python3


class Stack:
    '''Stack implementation'''
    def __init__(self):
        self._items = []
    def is_empty(self):
        return self._items == []
    def size(self):
        return len(self._items)
    def push(self, new_item):
        self._items.append(new_item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]


class StackError(Exception):
    '''Stack errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class TokenError(Exception):
    '''Token errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def rev_string_simple(my_str):
    '''Reverse characters in a string without using a stack'''
    return my_str[::-1]

def rev_string_stack(my_str):
    '''Reverse characters in a string using a stack'''
    new_str = Stack()
    for i in my_str:
        new_str.push(i)
    rev_str = []
    while not new_str.is_empty():
        rev_str.append(new_str.pop())
    return ''.join(rev_str)

def par_checker(line):
    '''Textbook implementation'''
    s = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        i = i + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def par_checker_file(filename):
    '''Check expresstions in the file'''
    with open(filename, 'r') as file_in:
        for line in file_in:
            line = line.strip()
            if par_checker(line) == True:
                print(line + ' ' + 'is balanced')
            else:
                print(line + ' ' + 'is NOT balanced')

def base_converter(dec_num, base):
    '''Convert any decimal number to any base'''
    # hex_digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    digits = '0123456789ABCDEF'
    remStack = Stack()
    if base in [2,8,16]:
        while dec_num > 0:
            rem = dec_num % base
            remStack.push(rem)
            dec_num = dec_num // base

    new_str = ''
    while not remStack.is_empty():
        new_str = new_str + digits[remStack.pop()]
    return new_str

def rpn_calc(postfix_expr):
    '''Evaluate a postfix expression'''
    operandStack = Stack()
    tokenList = postfix_expr.split()
    for token in tokenList:
        print(token)
        if token in '123456789':
            operandStack.push(int(token))
        elif token not in ['+','-','*','/']:
            raise TokenError("Unknown token: {}".format(token))
        else:
            if operandStack.size() > 1:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = do_math(token,operand1,operand2)
                operandStack.push(result)
            else:
                raise StackError('Stack is empty')
    if operandStack.size() == 1:
        return operandStack.pop()
    else:
        raise StackError('Stack is not empty')


def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    else:
        raise TokenError("Unknown operation: {}".format(op))
