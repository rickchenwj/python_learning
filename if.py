number=23
guess = int(raw_input('Enter an integer:'))

if guess == number:
	print'Congratulations,you guessed it.' #new block starts here
	print"(but you do not win any prizes!)" #new block ends here
elif guess < number:
	print'no,it is a little higher than that'#another block
	#you can do whatever you want in a block...
else:
	print'no,it is a little lower than that'
	#you must gusee>number to reach there

print 'Done'
#This is statement is always executed.after the is statement is excuted
