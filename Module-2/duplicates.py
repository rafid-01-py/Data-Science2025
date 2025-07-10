numbers = [1, 5, 6, 5, 1, 2, 3]

def find_duplicates(list):
    duplicates = []
    seen = set()
    for item in list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
 

print("Duplicates:", find_duplicates(numbers))
