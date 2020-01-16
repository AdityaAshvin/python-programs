def selection_sort(a):
    for i in range(len(a)):
        j=a.index(min(a[i:]))
        a[i],a[j]=a[j],a[i]
    return a

n=int(input())
a=[]
for i in range(n):
    a1=int(input())
    a.append(a1)
print(selection_sort(a))
