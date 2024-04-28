class stack:
    def __init__(self):
        self.stack=[]
        self.size=5
        self.top=-1
    
    def push(self,item):
        if self.top<self.size-1:
            self.stack.append(item)
            self.top +=1
        else:
            print("stack is overflow")
         
    def display(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])
            
        
    def pop(self):
       
         if self.isEmpty():
             print("under flow")
          
         else:   
            self.stack.pop()
            self.top-=1
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
        
obj=stack()
obj.push(3)
obj.push(2)
obj.push(9)
obj.push(5)
obj.pop()
obj.display()
