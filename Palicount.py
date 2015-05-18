#Pragramming taask given to Micahel for interview:
#Code to find longest palindrome in an entered string

#Ask user for string input
#Return the longest palindrome and its length

print ("Hello")

#Function returns true if parameters describe palindrome and false if not
def Palindrome(s,f): # s (f) is start (finish) index to check if palindrome
	answer = True #start with optimism
	while s<f:
		if theproblem[s] == theproblem[f]:
			s=s+1 #update squeeze play and tension
			f=f-1
		else:
			answer = False #only one step to determine not a palindrome
			s=f #kill check
	return answer #value of function call


global theproblem
theproblem = raw_input("Enter a string and I'll find the longest palindrome-->")
theproblem = str.lower(theproblem)
	
	
lastpos=len(theproblem)-1
#initialize counters and watcherz
maxlength=0
b=0
e=lastpos
bigb=0 #these keep track of position of largest palindrome found so far
bige=0
while maxlength<e-b+1: #keep looking until maxlength found is the same as leftover space to be searched
	while e>b: #move e towards b from right
		if Palindrome(b,e): 		# if b,e are a palindrome
			if e-b+1>maxlength:		# check then update length, incrememnt b, restart e
				maxlength=e-b+1
				bigb=b
				bige=e
			e=b
		else:
			e=e-1 #keep looking with this b
	b=b+1
	e=lastpos


print ("The longest Palindrome in " + theproblem + " is " + theproblem[bigb:bige+1])



