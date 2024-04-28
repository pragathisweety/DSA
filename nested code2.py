class A:
    def __init__(self):
        self.b=self.B()
    class B:
        def __init__(self): 
            self.c=self.C()
    class C:
        def __init__(self):
            print("deeksha")

A()