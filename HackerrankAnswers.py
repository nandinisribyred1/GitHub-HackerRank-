#=============Question 1======================
n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if command[0] == 'append':
        stack.append(int(command[1]))
    elif command[0] == 'print':
        print(stack)
    elif command[0] == 'insert':
        stack.insert(int(command[1]), int(command[2]))
    elif command[0] == 'remove':
        stack.remove(int(command[1]))
    elif command[0] == "pop":
        if stack:
            stack.pop()
    elif command[0] == "sort":
        stack.sort()
    elif command[0] == 'reverse':
        stack.reverse()
#==================Question 2=================
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

#====================Question 3===============
def average(array):
    array=set(array)
    return sum(array) / len(array)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
#=================Question 4====================
# Enter your code here. Read input from STDIN. Print output to STDOUT0
N=int(input())
sta=[]
stack=set(sta)

for _ in range(N):
    country=input()
    stack.add(country)
print(len(stack))    
#================Question 5====================
n = int(input())
stack = list(map(int, input().split()))
N=int(input())
for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        if stack:
            stack.pop(0)
    elif command[0] == 'remove':
        if int(command[1]) in stack:
            stack.remove(int(command[1]))
    elif command[0] == 'discard':
        if int(command[1]) in stack:
            stack.remove(int(command[1]))

print(sum(stack))
#================Question 6=======================
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
n1=set(map(int,input().split()))
b=int(input())
b1=set(map(int,input().split()))

sete=[]
sete=n1&b1

print(len(sete))
#=================Question 7======================
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
n1=set(map(int,input().split()))
b=int(input())
b1=set(map(int,input().split()))

sete=[]
sete=n1&b1

print(len(sete))
#=================Question 8======================
n=int(input())
for _ in range(n):
    n1=int(input())
    set1=set(map(int,input().split()))
    n2=int(input())
    set2=set(map(int,input().split()))
    if set1.issubset(set2):
        print("True")
    else:
        print("False")    
#===============Question 9=========================
# Enter your code here. Read input from STDIN. Print output to STDOUT
mset = set(map(int, input().split()))
n=int(input())
set1 = set(map(int, input().split()))
set2=set(map(int,input().split()))
if set1.issubset(mset) and set2.issubset(mset):
    print("True")
else:
    print("False")
#===============Question 10=========================
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

hap = 0
for element in array:
    if element in A:
        hap += 1
    if element in B:
        hap -= 1

print(hap)