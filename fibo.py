def fib():
	a,b,c,n=-1,1,0,int(raw_input("Enter position="))
	for i in range(n):
		c=a+b
		b,a=c,b
	print c

if __name__=='__main__':
	fib()
