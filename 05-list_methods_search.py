# Métodos de búsqueda

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list)

# index
print(numbers_list.index(3))  # busca un valor y regresa su indice dentro de la lista
print(
    numbers_list.index(3, 0, 4)
)  # busca un valor, entre el indice 0 y el 4-1 y regresa su indice dentro de la lista

# in
print(2 in numbers_list)
print(10 in numbers_list)

# count
print(
    numbers_list.count(2)
)  # cuenta cuantas veces se encuentra en la lista el valor mencionado
print(numbers_list.count(10))
