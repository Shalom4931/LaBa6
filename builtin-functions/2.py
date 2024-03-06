def count_upper(string):
    upper_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1;
    return upper_count

string = input()
upper = count_upper(string)

print (upper)