class ece:
    def __init__(self,*marks):
        self.m1=marks[0]
        self.m2=marks[1]
        self.m3=marks[2]
        self.m4=marks[3]
        self.m5=marks[4]
        
    def total(self):
        self.total=self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        print(self.total)
    
    def percentage(self):
        self.percentage=self.total/500*100
        print(self.percentage)
        
    def ranking(self,other):
        if self.total>other.total:
            print(" pacchu is 1st rank")
        else:
            print("deeksha is 1st rank")
    
pacchu=ece(100,100,100,100,98)
deeksha=ece(56,89,45,67,98,32)
pacchu.total()
deeksha.total()
pacchu.percentage()

ece.ranking(self=pacchu,other=deeksha)