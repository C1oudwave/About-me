from random import randint
mass = [randint(-100,100) for i in range(30)]
odd_mass = []
max_mass = max(mass)
index_of_max = mass.index(max_mass)
print("Max: ", max_mass, " Index: ", index_of_max)
def odd_list(mass, odd_mass):
    for i in range(len(mass)):
        if mass[i] % 2 != 0:
            odd_mass.insert(0, mass[i])
odd_list(mass, odd_mass)
temp = sorted(odd_mass, reverse = True)
print("New array:", temp)
