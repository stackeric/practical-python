def generator_n(n):
    while n > 0:
        yield n
        n -= 1


for i in generator_n(10):
    print(i)
    
