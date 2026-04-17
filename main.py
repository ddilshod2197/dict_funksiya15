def filter_range(d, min_val, max_val):
    return {k: v for k, v in d.items() if min_val <= v <= max_val}

def sum_range_values(d, min_val, max_val):
    filtered = filter_range(d, min_val, max_val)
    return sum(filtered.values())

data = {'a': 10, 'b': 20, 'c': 15, 'd': 25}
print(filter_range(data, 15, 25))      # {'b': 20, 'c': 15, 'd': 25}
print(sum_range_values(data, 15, 25))  # 60
