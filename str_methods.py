name = 'Swaroop'#this is a string object

if name.startswith('Swa'):
	print 'Yes, the string start with "Swa"'

if 'a' in name:
	print 'Yes, the string starts with "Swa"'

if name.find('War') != -1:
	print 'Yes, it contains the string "War"'

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print delimiter.join(mylist)

