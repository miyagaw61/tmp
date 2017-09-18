class deco_class:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("hoge")
        self.func(args[0])
        print("fuga")

@deco_class
def decolated(strings, arg="C"):
    """
    decolated("B", arg="C") ==
    deco_class(decolated)("B", arg="C")
    """
    print("A")
    print(strings)
    print(arg)
    print("D")

def func(*args):
    print(args[0])

class tmp_class:
    def __init__(self):
        self.tmp = "tmp"

    def __call__(self, arg):
        print(arg)

