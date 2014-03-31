def fib():
	a,b,c,rl,n=-1,1,0,[],int(raw_input("Enter position="))
	for i in range(n):
		c=a+b
		b,a=c,b
		rl.append(c)
	print rl[-1]

if __name__=='__main__':
	fib()
