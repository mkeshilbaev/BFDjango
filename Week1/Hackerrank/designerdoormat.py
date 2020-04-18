n, m = [int(x) for x in input().split()]
line = n // 2 + 1
x = 1
mk = (m-7) // 2
for i in range(1, n+1):
    middle = '.|.' * x
    k = (m - x * 3) // 2

    if line > i:    
        x += 2
    elif line < i:
        x -= 2
    borders = '-' * k
    
    if line == i:
        borders = '-' * mk
        print(borders + 'WELCOME' + borders)
        x -= 2
    else:
        print(borders + middle + borders)