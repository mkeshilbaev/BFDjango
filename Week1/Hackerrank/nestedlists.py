ls = []
for i in range(int(input())):
    name = input()
    score = float(input())
    ls.append([name, score])
second = sorted(set([score for name, score in ls]))[1]
for name, score in sorted(ls):
    if score == second:
        print(name)