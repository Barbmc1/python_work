for value in range(1,5):
	print(value)
	
print("\n")

numbers = list(range(1,6))
print(numbers)

print("\n")

even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)

print("\n")

squaress = []
for value in range(1,11):
	squaress.append(value**2)
	
print(squaress)

print("\n")

squares_list = [value**2 for value in range(1,12)]
print(squares_list)
