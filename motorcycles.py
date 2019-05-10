motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
print("\n")

motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

motorcycles2.insert(0, 'ducati')
print(motorcycles2)

print("\n")

del motorcycles[1]
print(motorcycles)
print("\n")

popped_motorcycles2 = motorcycles.pop()
print(motorcycles2)
print(popped_motorcycles2)

print("\n")

last_owned = motorcycles2.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".")

print("\n")
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

print("\n")
motorcycles2.append("ducati")
print(motorcycles2)

print("\n")
too_expensive = 'ducati'
motorcycles2.remove(too_expensive)
print(motorcycles2)
print("\nA " + too_expensive.title() + " is too expensive for me.")
