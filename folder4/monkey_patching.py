class A:
    def a():
        print("heet")

def b(self):
    print("meet")
    return "meet"

A.a=b
obj=A()
print(obj.a())   