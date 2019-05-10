my_foods = ['pizza', 'ice cream', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are : ")
print(friend_foods)

my_foods.append("cookies")
friend_foods.append("candy")
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are : ")
print(friend_foods)

print("\n")
barb_foods = my_foods
print("My favorite foods are: ")
print(my_foods)
print("Barb's favorite foods are: ")
print(barb_foods)

print("\n")
barb_foods.append("cheese")
print("My favorite foods are: ")
print(my_foods)
print("Barb's favorite foods are: ")
print(barb_foods)
