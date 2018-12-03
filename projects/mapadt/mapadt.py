'''Implementation of the Map ADT as HashTable'''

class HashTable:
    def __init__(self, size_init: int=16):
        '''Constructor'''
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        '''__getitem__'''
        return self.get(key)

    def __setitem__(self, key: int, value):
        '''__setitem__'''
        self.put(key, value)
    
    def __len__(self):
        '''__len__'''
        n = 0
        for value in self._values:
            if value is None: continue
            n += 1
        return n
    
    def __contains__(self, key):
        '''__contains__'''
        return key in self._keys

    def __str__(self):
        '''__str__'''
        data = [(k, str(self.get(k)))  for k in self.keys()]
        return '{}' if not data else '{'+', '.join("{}: '{}'".format(repr(k), v) for k,v in data)+'}'
        

    def _hash(self, key: int, size: int):
        '''Simple hash function'''
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int=1):
        '''Simple or quadratic rehash'''
        return (old_hash + step * step) % size

    def put(self, key: int, value):
        '''Add or update an item'''
        
        hashvalue = self._hash(key,len(self._keys))
    
        counter = 0
        step = 1
        if self._keys[hashvalue] == None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
            return
        else:
            if self._keys[hashvalue] == key:
                self._values[hashvalue] = value  #replace
            else:
                nextslot = self._rehash(hashvalue,len(self._keys))
                while self._keys[nextslot] is not None and self._keys[nextslot] != key and counter <= self._size:
                    nextslot = self._rehash(hashvalue,len(self._keys), step)
                    step +=1
                    counter += 1
                if self._keys[nextslot] == None:
                    self._keys[nextslot] = key
                    self._values[nextslot] = value
             
                else:
                    self._values[nextslot] = value #replace

        if None not in self._values:
            raise IndexError("Hash Table is full")
        

    def get(self, key: int):
        '''Retrieve an item'''
        startslot = self._hash(key,len(self._keys))
  
        value = None
        # stop = False
        # found = False
        position = startslot
        counter = 0
        step = 1
        while counter <= self._size:
            if self._keys[position] == key:
                # found = True
                value = self._values[position]
            else:
                position=self._rehash(startslot,len(self._keys), step)
                step += 1
            counter += 1
               
        return value

    def keys(self):
        '''Return all keys'''
        return [i for i in self._keys if i]

    def values(self):
        '''Return all values'''
        return [i for i in self._values if i]
        
    def items(self):
        '''Return all items'''
        data = [(k, str(self.get(k)))  for k in self.keys()]
        return data

