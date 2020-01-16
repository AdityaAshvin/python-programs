r=int(input())
c=int(input())
matrix=[]
for i in range(r):                 #making the matrix
    a=[]
    for j in range(c):
        a1=int(input("enter an element"))
        a.append(a1)
    matrix.append(a)
print(matrix)
for i in range(r):                 #printing the matrix
    for j in range(c):
        print(matrix[i][j],end="")
    print()

s=0
for i in range(r):                  #sum of all elements
    for j in range(c):
        s=s+matrix[i][j]
print("sum of all elements is ",s)

l=[]              
for k in matrix:                 #sum of elements of each row
    print(sum(k))

for k1 in matrix:              #max sum of rows
    a=sum(k1)
    l.append(a)
print("max sum of any row=",max(l))

for i in range(c):      #sum of elements in a column
    s2=0 
    for j in range(r):
        s2=s2+matrix[j][i]
    print(s2)

z=[]                        #max sum of columns
for i in range(c):
    s3=0
    for j in range(r):
        s3=s3+matrix[i][j]
        z.append(s3)
print("max sum of any column = ",max(z))
