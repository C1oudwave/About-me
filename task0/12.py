from random import randint
mass = [randint(-100,100) for i in range(30)]
max_mass = max(mass)
index_of_max = mass.index(max_mass)
print("Max: ", max_mass, "\nIndex of max: ", index_of_max)
def odd(mass):
    temp_mass = []
    for i in range(len(mass)):
        if mass[i] % 2 != 0:
            temp_mass.insert(0, mass[i])
    return temp_mass
mass = odd(mass)
sorted_mass = sorted(mass, reverse = True)
print("Sorted array:", sorted_mass)
