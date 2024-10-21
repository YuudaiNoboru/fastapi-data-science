from random import randint, seed

seed(10)
random_elements = [randint(1, 10) for I in range(5)]
print(random_elements)