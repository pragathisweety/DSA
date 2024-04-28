L=[1,2,45,67,7,5]
key=45
for i in range(len(L)):
    if L[i]==key:
        print(f"the value found at{i}thn index")
        break
if key not in L:
    print("the value is not found")



l=list(map(int,input("enter the list value").split(" ")))
key=int(input("enter the key value"))    
for i in range(len(l)):
     if l[i]==key:
            print(f"the value found at {i} thn index")
            break
if key not in l:
        print("the value is not found")