def fib():
	a,b,n=-1,1,int(raw_input("Enter position="))
	for i in range(n):
		b,a=a+b,b
	print b

if __name__=='__main__':
	fib()
