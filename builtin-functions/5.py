def all_true(tuple_values):
    return all(tuple_values)

input_string = input()

tuple_values = tuple(bool(int(x)) for x in input_string.split())

print(all_true(tuple_values))