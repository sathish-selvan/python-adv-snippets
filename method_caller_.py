from operator import methodcaller

names : list[str] = ['saathish', 'nithish', 'ranjith']
starts_with_s : methodcaller = methodcaller("startswith","s")

filtered : filter = filter(starts_with_s, names)

print(list(filtered))

count_a : methodcaller = methodcaller("count", "a")
sorted_list = sorted(names, key=count_a)
print(f'{sorted_list =}')