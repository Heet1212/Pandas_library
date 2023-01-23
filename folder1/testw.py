

def f(x):
    def f1(a, b):
        print("a",a,b)
        print("hello")
        if b==0:
            print("NO")
            return
        return g(a,b)
    return f1
#@f
def g(a, b):
    print("shah")
    return a%b


f=f(f)
print(f(4,2))   

