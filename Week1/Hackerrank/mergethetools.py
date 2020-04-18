def merge_the_tools(string, k):
    # your code goes here
    subs = []
    for i in range(0, len(string)-k+1, k):
        new_str = ''
        for j in string[i:i+k]:
            if j not in new_str:
                new_str += j
        subs.append(new_str)
    for i in subs:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)