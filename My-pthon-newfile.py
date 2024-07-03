year = int(input('Enter the year:'))
 if year % 4 and year % 100 and year % 400 == 0:
 	print('yes it s leap year')
else: 
 	print('it s not leap year')