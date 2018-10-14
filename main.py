print("hello world")

for x in "hello sudo":
	print (x)
	if x == "o":
		break
numbers = []
for x in range(0, 1000, 10):
	numbers.append(x)

for x in range(0, len(numbers), 1):
	print(numbers[x])