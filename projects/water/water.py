'''Water jugs project'''
#!/usr/bin/env python3
#encoding: UTF-8


JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    '''State of the jugs'''
    def __init__(self, jug_1: int, jug_2: int):
        '''__init__'''
        self._jug_1 = jug_1
        self._jug_2 = jug_2
    
    @property
    def jug_1(self):
        return self._jug_1
    
    @property
    def jug_2(self):
        return self._jug_2

    def __eq__(self, other: object):
        '''__eq__'''
        return self._jug_1 == other.jug_1 and self._jug_2 == other.jug_2

    def __str__(self):
        '''__str__'''
        return '(' + str(self._jug_1) + ', ' + str(self._jug_2) + ')'

    def clone(self):
        '''Copy a state'''
        new_jug_1 = self._jug_1
        new_jug_2 = self._jug_2
        return State(new_jug_1, new_jug_2)

    def fill_jug_1(self):
        '''Fill jug1 to capacity from the pump'''
        self._jug_1 = JUG_1_MAX

    def fill_jug_2(self):
        '''Fill jug2 to capacity from the pump'''
        self._jug_2 = JUG_2_MAX

    def empty_jug_1(self):
        '''Pour the water from jug1 onto the ground'''
        self._jug_1 = 0

    def empty_jug_2(self):
        '''Pour the water from jug2 onto the ground'''
        self._jug_2 = 0

    def pour_jug_1_to_jug_2(self):
        '''Pour as much water as you can from jug1 to jug2 without spilling'''
        measure = min(self._jug_1, JUG_2_MAX - self._jug_2)
        if measure > 0:
            self._jug_1 = self._jug_1 - measure
            self._jug_2 = self._jug_2 + measure        

    def pour_jug_2_to_jug_1(self):
        '''Pour as much water as you can from jug2 to jug1 without spilling'''
        measure = min(self._jug_2, JUG_1_MAX - self._jug_1)
        if measure > 0:
            self._jug_2 = self._jug_2 - measure
            self._jug_1 = self._jug_1 + measure        


def search(start_state: object, goal: object, moves_lst: list):
    '''Find a sequence of states'''
    moves_lst.append(start_state)
    if goal in moves_lst:
        return moves_lst
    else:
        case1 = start_state.clone()
        case1.fill_jug_1()

        case2 = start_state.clone()
        case2.fill_jug_2()

        case3 = start_state.clone()
        case3.empty_jug_1()

        case4 = start_state.clone()
        case4.empty_jug_2()

        case5 = start_state.clone()
        case5.pour_jug_1_to_jug_2()

        case6 = start_state.clone()
        case6.pour_jug_2_to_jug_1()

        if case1 in moves_lst:
            pass 
        else:
            return search(case1, goal, moves_lst)

        if case2 in moves_lst:
            pass 
        else:
            return search(case2, goal, moves_lst)

        if case3 in moves_lst:
            pass 
        else:
            return search(case3, goal, moves_lst)
        
        if case4 in moves_lst:
            pass 
        else:
            return search(case4, goal, moves_lst)
        
        if case5 in moves_lst:
            pass 
        else:
            return search(case5, goal, moves_lst)

        if case6 in moves_lst:
            pass 
        else:
            return search(case6, goal, moves_lst)


def main():
    '''Main function'''
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(', '.join([str(s) for s in moves]))


if __name__ == '__main__':
    main()
