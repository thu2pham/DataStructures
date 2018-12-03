'''
Reverse Polish Notation
Thu Pham - Project 3
'''
#!/usr/bin/env python3

import os.path # to check whether the file exists in your directory

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
        try:
            return self._items.pop()
        except IndexError:
            raise StackError('Stack is empty')

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

def postfix_eval(postfix_expr: str) -> int:
    # TODO: Evaluate an expression
    operandStack = Stack()
    tokenList = postfix_expr.split()
 
    result = 0
    for token in tokenList:
        
        if token.isdigit(): 
                operandStack.push(int(token))
        
        elif token in ['+','-','*','/','%','//','**']:
            if operandStack.size() > 1:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                if operand2 == 0:
                    try:
                        result = do_math(token,operand1,operand2)
                        operandStack.push(result)
                    except ZeroDivisionError:
                        if token == '/':
                            raise ZeroDivisionError('ERROR: division by zero')
           
                        else:
                            raise ZeroDivisionError('ERROR: integer division or modulo by zero')
                                                   
                else:
                        result = do_math(token,operand1,operand2)
                        operandStack.push(result)
                       
            else:
                raise StackError('Stack is empty')
                   

        elif token == '=':
        
            result = operandStack.pop()
            if operandStack.is_empty():
                return result
            else:
                raise StackError('Stack is not empty')
        
        else:
            raise TokenError('Unknown token: {}'.format(token))


def do_math(op: str, op1: int, op2: int) -> int:
    # TODO: Process arithmetic operations
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "//":
        return op1 // op2
    elif op == "%":
        return op1 % op2
    elif op == "**":
        return op1 ** op2
    else:
        raise Exception("Unknown operation: {}".format(op))


def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    checksum = []
    try:
        with open(filename, 'r') as file_in:
            for line in file_in:  
                # print(line)
                try:
                    result = postfix_eval(line)
                    print(line, result)
                    checksum.append(result)
                except Exception as e:
                    print(line, str(e))
        return sum(checksum)
             
    except IOError:
        print('There was an error opening the file')



def main():
    checksum = rpn_calc('data/projects/rpn/rpn_input_1.txt')
    print('Checksum is %.2f' % checksum)

main()
# if __name__ == '__main__':
#     main()
