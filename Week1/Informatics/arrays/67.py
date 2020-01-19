n = int(input())
arr = []
cnt = 0

for i in range(0, n):
    k = int(input())
    arr.append(k)

for i in range(0, n - 1):
    if arr[i] == arr[i+1]:
     print("YES")
    break

else:
    print("NO")

