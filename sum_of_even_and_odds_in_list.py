lst = [1, 2, 3, 4, 5, 6]
sum_evens = 0
sum_odds = 0
for num in lst:
    if num % 2 == 0:
        sum_evens += num
    else:
        sum_odds += num
print((sum_evens, sum_odds))
