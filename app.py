def counter(a,b): # кол-во целых чисел в промежутке от a до b
  summ = 0
  for i in range(a, b, 1) if a < b else range(b, a, 1):
    summ += 1
  return summ

a = int(input())
b = int(input())

print(counter(a,b))
