##Fibonacci function
##Input - x, specifying you want the xth number in the fibonacci sequence
##Output- F, the xth number of the fibonacci sequence

def fibonacci( x):
	if(int(x)==1): return 1;
	if(int(x)==2): return 1;
	F=1
	E=1	## a placeholder for the number 1 before F in the sequence
	f=0	## a return variable
	for num in range(1,int(x-1)):
		f=E+F;
		E=F
		F=f		
	return f;

n = input('Enter which fibonacci number you would like: ')
print 'The ' + str(n) + 'th number in the fibonacci sequence is ' + str(fibonacci(int(n)))

