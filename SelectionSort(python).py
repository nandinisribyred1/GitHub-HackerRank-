arr=[9,17,8,6,5]
n=len(arr)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]    

print(arr)        


#--------------SelectionSort(With recursion)----------------------
#def selection_sort(arr):
#      for i in range(len(arr)-1):
#           min=i
#           for j in range(i+1,len(arr)):
#                 if arr[j]<arr[min]:
#                       min=j
#           arr[i],arr[min]=arr[min],arr[i]
#      return arr
#arr=list(map(int,input().split()))
#print(selection_sort(arr))                