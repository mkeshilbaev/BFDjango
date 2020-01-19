n = int(input())
arr = []

for i in range(0, n):
    k = int(input())
    arr.append(k)

for i in range(0, n, 2): #step 2 means adding 2 index
    #if i % 2 == 0:
     print(arr[i])

