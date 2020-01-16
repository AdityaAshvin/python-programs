def linear_search(list,key):
    for i in range(len(list)):
        if(key==list[i]):
            return i
    return -1

list=[1,2,3,4,5,6,7]
key=int(input())
print(linear_search(list,key))
