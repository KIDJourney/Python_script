#coding=utf-8
#coded by KIDJourney
"""
main idea
well in python it's easy to cul something that can be saved as string

and the priority can be solved with the origin priority of opeartion
so the best way of solving the problem is to reload the opeartion 
"""
opdir={"->":"+","&":"/","|":"*","!":"-","(":"(",")":")"}  # the string to real op opeartion
obset=[]
obdir={}# the char to object
charlist=[]

class unit:
	def __init__(self,value):
		self.value=int()
		self.value=value
	def __add__(self,n): #+ same as ->
		if self.value>n.value:
			return unit(0)
		else:
			return unit(1)
	def __div__(self,n): #/ same as &
		if self.value&n.value:
			return unit(1)
		else:
			return unit(0)
	def __mul__(self,n): #* same as |
		if self.value|n.value:
			return unit(1)
		else:
			return unit(0)
	def __neg__(self): #pre - same as !
		return unit(1-self.value)
	def __str__(self):
		return str(self.value)
	def getvalue(self,n):
		self.value=int(n)
	def check(self):
		if self.value == 1:
			return True
		else:
			return False

def stringop(string):
	nop=0
	after_op=str()	
	i = 0
	while i <len(string):
		if charcheck(string[i]):
			# if string[i] in obdir.keys():
			# 	nop-=1
				# print "a char appear twice , input error ,plz try again"
				# exit()
			temp = unit(0)
			if  not string[i] in obdir.keys():
				charlist.append(string[i])
				nop+=1
			obdir[str(string[i])]=temp
			after_op+="obdir['"+string[i]+"']"
			i+=1
			continue
		if (string[i]=='-')and(string[i+1]=='>'):
			after_op+=opdir["->"]
			i+=2
			continue
		else:
			if string[i] in opdir.keys():
				after_op+=opdir[string[i]]
				i+=1
			else:
				print "input error,plz try again"
				exit()
	return (after_op,nop,len(string))

def charcheck(self):
	if (self>='A')&(self<='Z'):
		return True
	else:
		return False


def show(user_input,cul_string,numofmt,maxlen):
	"""
	user_input mean the origin input 
	cul_string mean the culuate string 
	numofmt  mean the num of char 
	maxlen mean what ? ohch i don't know
	"""
	main_xiqu=str()
	main_hequ=str()
	value = 2**numofmt
	print "numofmt = ",numofmt
	print "maxbit = ",value 
	print "cul_string = ",cul_string
	for i in charlist:
		print "{0:<10}".format(i),
	print ("{0:<%d}"% int(maxlen+10)).format(user_input)
	for i in range(value): #value add loop
		value_str=str('0'*int(numofmt-len(str(bin(i)[2:])))+bin(i)[2:])
		for j in range(numofmt):  
			obdir[charlist[j]].getvalue(int(value_str[j]))
		for j in charlist:
			print "{0:<10}".format(obdir[j]),
		print ("{0:<%d}"% int(maxlen+10)).format(eval(cul_string))
		#value - output end
		#zhu xi qu fan shi zhu he qu fan shi begin
		if eval(cul_string).check(): #zhu he qu
			main_xiqu+='v('
			for c in charlist[:-1]:
				if obdir[c].check():
					main_xiqu+=c+'&'
				else:
					main_xiqu+='!'+c+'&'
			if obdir[charlist[-1]].check():
				main_xiqu+=charlist[-1]
			else:
				main_xiqu+='!'+charlist[-1] 
			main_xiqu+=')'
		else:
			main_hequ+="&("
			for c in charlist[:-1]:
				if (not obdir[c].check()):
					main_hequ+=c+'v'
				else:
					main_hequ+='!'+c+'v'
			if not obdir[charlist[-1]].check():
				main_hequ+=charlist[-1]
			else:
				main_hequ+='!'+charlist[-1] 
			main_hequ+=')'
	print "main_xiqu is \n" , main_xiqu[1:]
	print "main_hequ is \n" , main_hequ[1:]


if __name__=="__main__":
	user_input = raw_input("plz input your mingti \n  ")
	cul_string , numofmt , maxlen= stringop(user_input)
	show(user_input,cul_string,numofmt,maxlen)
