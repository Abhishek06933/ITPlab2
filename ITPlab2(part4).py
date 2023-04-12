myNumbers = [3, 8, 12, 15, 21, 7, 10, 16]

def print_list(lst):
    for num in lst:
        print(num)

print_list(myNumbers)

print("Elements greater than 12:")
for num in myNumbers:
    if num > 12:
        print(num)
