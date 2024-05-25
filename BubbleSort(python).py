arr = [5, 2, 1, 3, 6, 9]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[i]
print("Sorted elements: ", arr)


#-----------------BubbleSort(With recursion)--------------
#def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#               if arr[j]>arr[j+1]:
#                    arr[j],arr[j+1]=arr[j+1],arr[i]
#     return arr
#arr=list(map(int,input().split()))
#print(bubble_sort(arr))  
