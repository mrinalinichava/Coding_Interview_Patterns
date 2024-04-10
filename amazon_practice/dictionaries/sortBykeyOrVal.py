my_dict = {'banana': 3, 'apple': 2, 'pear': 1, 'orange': 5}

# Sorting by key and creating a new dictionary
sorted_dict_by_key = dict(sorted(my_dict.items(), key=lambda item: item[0]))

print("Sorted by Key:", sorted_dict_by_key)


my_dict = {'banana': 3, 'apple': 2, 'pear': 1, 'orange': 5}

# Sorting by value and creating a new dictionary
sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted by Value:", sorted_dict_by_value)



my_dict = {'banana': 2, 'apple': 2, 'pear': 1, 'orange': 2}

# Sorting by value, then by key (assuming a scenario where this makes sense)
sorted_dict_by_value_then_key = dict(sorted(my_dict.items(), key=lambda item: (item[1], item[0])))

print("Sorted by Value, then by Key:", sorted_dict_by_value_then_key)
