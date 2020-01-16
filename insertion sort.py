def insertion_sort(a):
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while((j>=0)and(key<a[j])):
                a[j+1]=a[j]
                j=j-1
            a[j+1]=key
        return a
    
n=int(input())
a=[]
for i in range(n):
    a1=int(input())
    a.append(a1)
print(insertion_sort(a))
