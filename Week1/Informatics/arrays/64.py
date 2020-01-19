n = int(input())
arr = []

for i in range(0, n):
    k = int(input())
    arr.append(k)

for i in range(0, n):
    if arr[i] % 2 == 0:
     print(arr[i], end=" ")

