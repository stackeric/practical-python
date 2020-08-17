

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

manual_inter()

def inter_loop():
    arr = [1, 2, 3]

    it = iter(arr)

    try:
        while True:
            el = next(it)
            print(el)
    except StopIteration:
        pass


inter_loop()
