set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

union_result = set_A | set_B
intersection_result = set_A & set_B
difference_A_B = set_A - set_B
difference_B_A = set_B - set_A
 
rows = [
    ("Set A", str(set_A)),
    ("Set B", str(set_B)),
    ("Union (A ∪ B)", str(union_result)),
    ("Intersection (A ∩ B)", str(intersection_result)),
    ("Difference (A - B)", str(difference_A_B)),
    ("Difference (B - A)", str(difference_B_A))
]
 
print(f"{'Operation':<25} Result")
print("-" * 50)
for label, result in rows:
    print(f"{label:<25} {result}") 