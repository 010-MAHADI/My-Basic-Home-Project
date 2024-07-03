'''b = int(input('Enter the number: '))
number = 0
while number <= b :
	print(number)
	number = number + 1
'''
b = int(input('Enter the number: '))
for number in range(b + 1):
    print(number)
   
k = int(input('Enter the number: '))
for number in range(1, k + 1 ):
    print(number)


p = list(range(10, 101, 3))
print(p)