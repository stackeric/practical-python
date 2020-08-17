## Python Iterator 

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

### 1. 简单生成器

``` python
def generator_n(n):
    while n > 0:
        yield n
        n -= 1


for i in generator_n(10):
    print(i)
    

```

### 2. 手动迭代

``` python
def inter_loop():
    arr = [1, 2, 3]

    it = iter(arr)

    try:
        while True:
            el = next(it)
            print(el)
    except StopIteration:
        pass

```

### 3. 读文件

``` python
def manual_inter():
    with open("./manual_interator.py", "r") as f:
        print(type(f))
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            print("EOF")
            pass
```

### 4. 斐波那契数列

``` python
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
```

### 5. 深度优先遍历

``` python
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)

```