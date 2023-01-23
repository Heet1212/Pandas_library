def upper(f):

    def f1(a):
        
        return a.upper()


    return f1


@upper
def p(a):
    print('abcdclear')
    print(a)




print(p("heet"))

