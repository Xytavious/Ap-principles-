class Quicksort:
    @staticmethod
    def sort(a, low=0,high= None):
        if high is None:
            high = len(a)-1
        if low < high:
            pivot = Quicksort.partition(a,low,high)
            Quicksort.sort(a,pivot-1)
            Quicksort.sort(a,pivot+1, high)
        return a
    
    @staticmethod
    def partition(a,low,high):
        pivot = a[high]
        i = low-1
        for j in range(low,high):
            if a[j] <= pivot:
                i += 1
                Quicksort.swap(a,i,j)
        Quicksort.swap(a,i+1,high)
        return i+1
    
    @staticmethod
    def swap(a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp