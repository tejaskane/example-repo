a=250
def f1():
    #use global keyword to rewrite global variable
    global a
    a=100
    print(a)
def f2():
    b=a+10
    print(b)
f1()
f2()
print(a)
