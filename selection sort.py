l=[23,4,56,7,89,3,0,45,2,76]
n=len(l)
for i in range(n):
    min=i
    for k in range(i+1,n):
        if l[min]>l[k]:
            min=k
        l[i],l[min]=l[min],l[i]
print(l)