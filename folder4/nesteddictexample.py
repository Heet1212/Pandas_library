
nested_dict = {
    "A": 2,
    "B": 5,
    "C": {
        "A": 7,
        "B": 2
    }
}

total_sum = {}

def sum_same_key(d):
    for key, value in d.items():
        if isinstance(value, dict):
            sum_same_key(value)
        elif key in total_sum:
            total_sum[key] += value
        else:
            total_sum[key] = value

sum_same_key(nested_dict)
print(total_sum)
# Output: {'A': 9, 'B': 7}