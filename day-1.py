##Polymorphism - it means having many forms.In programming, polymorphism means same
##function name(but different signatures) being used for different types.
##The key difference is the data types and number or arguments used in function

def add(a,b,c=0):
    print(a+b+c)       ## here add fn is used for various types
add(1,2)
add(1,2,3)

class Animal:
    def sound(self):
        print("Animal makes a sound")
class dog(Animal):
    def sound(self):       ## polymorphism - method overriding
        print("Dog barks")
class bird(Animal):
    def sound(self):       ## polymorphism - method overriding
        print("Birds sing")

b1=bird()
b1.sound()

##super keyword
##
##class a():
##    def __init__(self):
##        print('A')
##    def display(self):
##        print('you are in class A')
##class b(a):
##    def __init__(self):
##        super().__init__()
##        print('B')
##    def display(self):
##        print('you are in class B')
##class c(b):
##    def __init__(self):
##        super().__init__()
##        print('C')
##    def display(self):
##        print('you are in class C')
##o1=c()



##a = int(input('enter a'))
##b = int(input('enter b'))
##m=int(input('enter m'))
##def add(n1,n2):
##    return  n1+n2
##c=add(a,b)
##print(c*m)
