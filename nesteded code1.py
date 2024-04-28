class A:
    class B:
        class C:
            a=78
obj=A()
obj1=obj.B()
obj2=obj1.C()
print(obj2.a)