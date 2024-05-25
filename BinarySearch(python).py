def Binary_search(ar,key):
    low=0
    high=len(ar)-1
    while low<=high:
        mid=(low+high)//2
        if ar[mid]==key:
            return mid+1
        elif ar[mid]<key:
            low=mid+1
        else:    
            high=mid-1
    return -1

arr=list(map(int,input("Enter elements:").split()))
arr.sort()
#print(arr)
key=int(input("Enter the key:"))
result=Binary_search(arr,key)
if result==-1:
    print("Element not found")
else:
    print("Element found at index ",result)    

#------------------------BinarySearch(Without Function)---------------------------#

#arr = list(map(int, input("Enter elements:").split()))
#arr.sort()
#key = int(input("Enter the key:"))
#low = 0
#high = len(arr) - 1
#while low <= high:
#    mid = (low + high) // 2
#   if arr[mid] == key:
#       print("Element found at index", mid)
#        break
#    elif arr[mid] < key:
#        low = mid + 1
#   else:
#       high = mid - 1
#if low > high:
#   print("Element not found.")
