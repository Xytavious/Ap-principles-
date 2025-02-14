class mergesort:
    @staticmethod
    def sort(a):
        if len(a) > 1:
            mid = len(a)/2
            l = a
            r = a
            mergesort(l)
            mergesort(r)
            mergesort(a,l,r)
class Merge:
    i = 0
    j =0
    k=0
    l =0
    r=0
    a=0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else a[k] = r[j]
