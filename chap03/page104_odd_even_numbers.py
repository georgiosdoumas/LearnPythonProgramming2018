from itertools import compress

N = 10
data = range(10)
even_selector = [1, 0] * (N//2)
odd_selector = [0, 1] * (N//2)
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)
