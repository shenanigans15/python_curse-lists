# Métodos de ordenamiento

letters = ["a", "b", "o", "c", "z", "g", "d", "e", "m"]
print(letters)

# sort
letters.sort()  # ordena alfabeticamente la lista
print(letters)

# sorted()
new_letters = sorted(letters)  # devuelve la lista ordenada como una nueva
print(new_letters)

# # con slicing
# new_letters = letters[:]
# new_letters.sort()

# # con copy
# new_letters = letters.copy()
# new_letters.sort()

# reverse
letters.reverse()
print(letters)
