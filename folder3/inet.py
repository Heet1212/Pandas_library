def f(x):

    def f1(*args):

        if args==0:
            print("no wrong value")
            return

        return x(*args)
    return f1 

@f
def g(a,b):

    return a%b

print(g(4,2))    