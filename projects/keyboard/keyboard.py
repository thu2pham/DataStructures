'''
Touchscreen Keyboard
'''
#!/usr/bin/env python3

import sys

def spell_check(filename: str) -> None:
    '''Rank words by their proximity to the target'''

    keyboard = """qwertyuiop
asdfghjkl
zxcvbnm"""
    order = {}
    lines = keyboard.split('\n')
    for ind, c in enumerate(lines):
        for i, ch in enumerate(c):
            order[ch] = (ind, i)
    # print(order)
    with open(filename, 'r') as file_in:
        lines = file_in.read().splitlines()
        file_in.close()
        
        
        lines.remove(lines[0])
        checker = []
        key = []
        l = []
        for line in lines:
            
            lst = line.split()
            
            if len(lst) > 1:
                part1 = lst[1]
                l.append(int(part1))
                part0 = lst[0]
                key.append(part0)
           
            else:
                
                checker.append(line)
    # print(checker)
    strings = {}
    # print(key)
    ''' Dictionary of typed and check list '''
    i = 0
    n = 0
    for value in l:
        chunks = [checker[i:i+int(value)]]
        i = i + int(value)
        strings[key[n]] = chunks
        n += 1
    
    
    for word in strings:
        for value in strings[word]:
            check_spell = []
            for item in value:
                sum = 0
                
                for ch1, ch2 in zip(item, word):
                    x1, y1 = order[ch1]
                    x2, y2 = order[ch2]
                    distance = abs(x1-x2) + abs(y1-y2)
                    sum = sum + distance 
                check_spell.append([item, str(sum)])

            check_spell.sort(key = lambda x: (int(x[1]), x[0]))
            for spell in check_spell:
                print(spell[0] + " " + str(spell[1]))
 

def main():
    '''Entry point'''
    filename = 'data/projects/keyboard/sample.in'
    print('Processing file {}'.format(filename))
    spell_check(filename)
        

if __name__ == '__main__':
    
    main()
