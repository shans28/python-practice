#convert Nested list to flat list 
lst = [1, [2, 3], [4, 5], 6]

flat_list = []

for item in lst:
    print(type(item))
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print(flat_list)
