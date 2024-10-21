from random import randint, seed

seed(10)

rando_unique_elements = {randint(1, 10) for i in range(5)}
print(rando_unique_elements)