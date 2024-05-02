from operator import itemgetter

numbers: list[int] = [3, 5, 2, 4, 7]
first_last_number : itemgetter = itemgetter(0,-1)
print(first_last_number(numbers))
