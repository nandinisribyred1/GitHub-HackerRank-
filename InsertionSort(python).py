arr=[9,6,4,8,2,1]
for i in range(1, len(arr)):
    key=arr[i]
    j=j-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)    
