def binary_search(list,key):
    low=0
    end=len(list)-1
    while(end>=low):
        mid=(low+end)//2
        if(key<list[mid]):
            end=mid-1
        elif(key>list[mid]):
            low=mid+1
        else:
            return mid
    return "NOT FOUND"

list=[1,2,3,4,5]
key=int(input())
print(binary_search(list,key))

