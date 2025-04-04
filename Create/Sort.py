class mergesort:
    @staticmethod
    def sort(a):
        if len(a) > 1:
            mid = len(a)/2
            l = a[:mid]
            r = a[mid:]
            mergesort(l)
            mergesort(r)
            mergesort(a,l,r)
    
    @staticmethod
    def Merge(A,L,R):
        i = 0
        j =0
        k=0
       
        while i < len(L) and j < len(R):
            if L[i] < [j]:
                A[k] = L[i]
                i += 1
            else :
                A[k] = R[j]
                j+=1
            k +=1
             
            while i <len(L):
                A[k] = L[i]
                i +=1
                k +=1

            while j <len(R):
                A[k]=R[j]
                j+=1
                k+=1