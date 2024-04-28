List=[4,6,9,2,1,0]
def merge(List):
    if len(List)>1:
        mid=len(List)//2
        left=List[:mid]
        right=List[mid:]
        merge(left)
        merge(right)
        L=0
        R=0
        K=0
        while L<len(left) and R<len(right):
            if left[L]>right[R]:
                List[K]=right[R]
                R=R+1
            else:
                List[K]=left[L]
                L=L+1
                K=K+1
            
        while L<len(left):
            List[K]=left[L]
            L=L+1
            R=R+1
        while R<len(right):
           List[K]=right[R]
           R=R+1
           K=K+1
           
               
        
        