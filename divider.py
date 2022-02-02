def divider(num):
    for i in range(1, num+1):
        if num % i == 0:
            yield i
n = int(input())
a = divider(n)
for i in a:
    print(i, end=' ')

