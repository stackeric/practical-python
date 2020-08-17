
class Fibonacci:

    def __init__(self, n):
        self._a = 0
        self._b = 1
        self.n = n
        self.loop = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop <= self.n:
            self._a, self._b = self._b, self._a + self._b
            self.loop += 1
            return self._a
        else:
            raise(StopIteration)


for i in Fibonacci(10):
    print(i)
