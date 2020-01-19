def minimal(a, b, c, d):
    mini = a
    if (b < mini):
        mini = b
    if (c < mini):
        mini = c
    if (d < mini):
        mini = d

    print(mini)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    minimal(a, b, c, d)
