Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input("How many terms?"))
How many terms?15
>>> n1,n2=0,1
>>> count=0
>>> if n<=0:
	print("Enter a positive integer")
elif n==1:
	print("Fibonacci sequence upto",n,":")
	print(n1)
else:
	print("Fibonacci sequence:")
	while count<n:
		print(n1)
	nth=n1+n2
	n1=n2
	n2=nth
	count+=1
	