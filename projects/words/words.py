'''Build a ladder of words using stacks and queues'''
#!/usr/bin/env python3

WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()


class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []
    def size(self):
        '''Return stack size'''
        return len(self.items)
    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)
    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()
    def peek(self):
        '''Look at the top item'''
        return self.items[-1]
    def clone(self):
        '''Cloning a stack'''
        stack_clone = Stack()
        stack_clone.items = self.items[:]
        return stack_clone


class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)


def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    myword = open(filename, 'r')
    d = {}
    for line in myword:
        word = line.rstrip()
        if len(word) == 3:
            WORDS_OF_3.add(word)
        elif len(word) == 4:
            WORDS_OF_4.add(word)
        elif len(word) == 5:
            WORDS_OF_5.add(word)
    d[3] = len(WORDS_OF_3)
    d[4] = len(WORDS_OF_4)
    d[5] = len(WORDS_OF_5)
    return d

def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    count = 0
    for ch1, ch2 in zip(word1, word2):
        if ch1 != ch2:
            count += 1
    return count


def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    words = []
    for each_word in all_words:
        if distance(word, each_word) == 1 and each_word not in used_words:
            words.append(each_word)
    return words

def main():
    '''Main function'''
    read_file('data/projects/words/words.txt')

    word_start = 'stone'
    word_stop = 'water'
    found = False
    if len(word_start) != len(word_stop):
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    if (len(word_start)) == 3:
        words_to_use = WORDS_OF_3
    elif (len(word_start)) == 4:
        words_to_use = WORDS_OF_4
    elif (len(word_start)) == 5:
        words_to_use = WORDS_OF_5
    else:
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    
    print("Let's turn '%s' into '%s'" % (word_start, word_stop))
    # TODO: Implement the algorithm
    
    found = False

    used_words = set()
    used_words.add(word_start)
    
    initial_words_stack = Stack()
    initial_words_stack.push(word_start)

    initial_words_queue = Queue()
    initial_words_queue.enqueue(initial_words_stack)

    while not found and not initial_words_queue.is_empty(): 
        stack_dequeue = initial_words_queue.dequeue()
        if stack_dequeue.peek() == word_stop:
            found = True
        else:
            candidate_lst = diff_by_one_all(stack_dequeue.peek(), words_to_use, used_words)
            for word in candidate_lst:
                stack_clone = stack_dequeue.clone()
                stack_clone.push(word)
                used_words.add(word)
                initial_words_queue.enqueue(stack_clone)


    if found:
        print('Ladder found!')
        # TODO: Print the ladder
        lst = []
        for i in range(0, stack_dequeue.size()):
            lst.append(stack_dequeue.pop())
            
        for words_ladder in lst:
            print(words_ladder)
    else:
        print('Ladder not found')


if __name__ == '__main__':
    main()
