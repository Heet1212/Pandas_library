def foo():
    try:
     return 1
    finally:
        return 2

def h():
    return foo()
k =h()
print(k)