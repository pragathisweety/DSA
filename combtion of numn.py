l=[1,2,3,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])
            
            
            
            
l=[1,2,3,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range (j+1,len(l)):
            print(l[i],l[j],l[k])