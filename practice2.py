r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a1=int(input("enter a element"))
        a.append(a1)
    matrix.append(a)

for k in matrix:
    print(sum(k))

for i in range(c):
    s=0
    for j in range(r):
        s=s+matrix[j][i]
    print(s)
