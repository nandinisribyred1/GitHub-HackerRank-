def linear_search(ar,key):
    for i in range(len(ar)):
        if ar[i]==key:
            return i+1
    return -1    
        
arr=list(map(int,input("Enter elements:").split()))
key=int(input("Enter key:"))
result=linear_search(arr,key)
if result!=-1:
    print("Element found at index",result)
else:
    print("Element not found.")    


#-------------LinearSearch(Without recursion)------------------
#arr=list(map(int,input("Enter elements:").split()))
#key=int(input("Enter key:"))
#for i in range(len(arr)):
#       if arr[i]==key:
#            c=c+1
#            flag=1
#if flag==1:
#     print("Element found at index:",c)
#else:
#     print("Element not found")
