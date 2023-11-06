class Stack:
    def __init__(self):
        self.stack = []
        self._max = None

    def pop(self):
        if self.is_empty():
            return None
        removed = self.stack.pop()
        if self.is_empty():
            self._max = None
        elif removed == self._max:
            self._max = self.stack[0]
            for val in self.stack:
                if val > self._max:
                    self._max = val
        return removed

    def push(self, item):
        self.stack.append(item)
        if self.size() == 1 or item > self._max:
            self._max = item

    def is_empty(self):
        if self.size() == 0:
            return True

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[self.size() - 1]

    def get_max(self):
        return self._max
