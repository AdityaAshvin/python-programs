def fibbonacci(n):

    for j in range(3,n):
        s=0
        a=1
        b=2
        s=s+a+b
        a=b
        b=s
    return b
    return s
    even(b)

def even(n):
    se=0
    if(n%2==0):
        se=se+n
    return se

T = int(input())
s=0
se=0
for i in range(T):
    n = int(input())
    fibbonacci(n)
    print(even(se))
    
    

