set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 41}

set_diff1 = set1 - set2
set_diff2 = set2 - set1

print("Set Difference")
print( "(set1 - set2):", set_diff1)
print( "(set2 - set1):", set_diff2)
print(" ")

union_set = set1 | set2
print("Union of sets")
print("(set1 | set2):", union_set)
print(" ")

sym_diff1 = set2 ^ set1
sym_diff2 = set1 ^ set2
print("Symmetric Difference")
print("(set2 ^ set1):", sym_diff1)
print("(set1 ^ set2):", sym_diff2)
print(" ")

intersection_set1 = set1 & set2
intersection_set2 = set2 & set1
print("Set Intersection")
print("(set1 & set2):", intersection_set1)
print("(set2 & set1):", intersection_set2)