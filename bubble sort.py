def bubble_sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[]
n=int(input())
for i in range(n):
    a1=int(input())
    a.append(a1)
print(bubble_sort(a))
