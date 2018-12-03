"""Limited size max Binary Heap implementation"""
#!/usr/bin/env python3


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while (cur_idx - 1) // 2 >= 0:
            par_idx = (cur_idx - 1) // 2
            if self.heap[cur_idx] > self.heap[par_idx]:
                self.heap[cur_idx], self.heap[
                    par_idx] = self.heap[par_idx], self.heap[cur_idx]
            else:
                return
            cur_idx = par_idx

        
    def perc_down(self, cur_idx):
        """Moving a node down"""
        while 2 * cur_idx + 1 < len(self.heap):
            smaller_child_idx = self.get_max_child(cur_idx)
            if self.heap[cur_idx] > self.heap[smaller_child_idx]:
                self.heap[cur_idx], self.heap[smaller_child_idx] = self.heap[
                    smaller_child_idx], self.heap[cur_idx]
            else:
                return
            cur_idx = smaller_child_idx
 

    def insert(self, item):
        """Adding a new item"""

        if self.max_size == 0:
            self.heap.append(item)
            self.size = self.size + 1
            self.perc_up(self.size - 1)
        else:
            
            if self.size < self.max_size:
                self.heap.append(item)
                self.size = self.size + 1
                self.perc_up(self.size - 1)              
            else:
                smallest = min(self.heap)
                if item > smallest:
                    self.heap.remove(smallest)
                    self.heap.append(item)
                    self.perc_up(self.size - 1)

    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        if 2 * parent_idx + 2 > self.size - 1:
            return 2 * parent_idx + 1
        else:
            if self.heap[2 * parent_idx + 1] > self.heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            else:
                return 2 * parent_idx + 2

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)
