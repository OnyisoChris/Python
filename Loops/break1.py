no = int(input('Enter any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num == no:
        print ('Number found in list')
        break
else:
        print ('Number not found in list')