def f(x):
    def f1(*args,**kwargs):
        x(*args,**kwargs)
        print("*"*5)
       
        print("*"*5)

    return f1
def a(x):
    def f1(*args,**kwargs):
        
         print("%"*5)
        
         print("%"*5)   
         x(*args,**kwargs)
    return f1


@f
@a
def p(m):

    print("heet")
    print(m)

p('hello')