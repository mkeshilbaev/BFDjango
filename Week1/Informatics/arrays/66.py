n = int(input())
arr = []
cnt = 0

for i in range(0, n):
    x = int(input())
    arr = [int(x) for x in input().split()]

    #arr.append(k)

for i in range(0, n - 1):
    if arr[i] < arr[i+1]:
     cnt = cnt + 1

print(cnt)

