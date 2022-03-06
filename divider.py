def divider(num):
  # генератор делителей  
  for i in range(1, num+1):
        if num % i == 0:
            yield i
# ввод делимого  
n = int(input())
a = divider(n)
# вывод ряда делителей 
for i in a:
    print(i, end=' ')

