lst = [1, 2, 3, 4, 5, 6]
evens = []
odds = []
for num in lst:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(evens)
print(odds)
