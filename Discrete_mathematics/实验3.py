class Graphics:
	def __init__(self):
		self.size = 0
		self.graphics = []
		self.shallg = []
		self.judge = 0  # 1 QL 2 dL 3 RL 4 BL
		self.graType = ['0','QL',"DL","RL","BL"]

	def userinput(self):
		self.size = int(raw_input("Please input the size of Graphics\n"))
		for i in range(self.size):
			temp = list(map(int,(raw_input().strip()).split(" ")))
			self.graphics.append(temp)

	def warshall(self):
		copy = self.graphics[:]
		k = 0
		while(k<self.size) :
			for i in range(self.size):
				if copy[i][k] != 0:
					for j in range(self.size):
						copy[i][j] = copy[i][j] or copy[k][j]
			k += 1
		self.shallg = copy[:]
		print "reachability matrix"
		self.show(copy)

	def show(self,gra):
		size = len(gra)
		for i in range(size) :
			for j in range(size) :
				print gra[i][j] ,
			print ''

	def judugGrap(self):
		copy = self.shallg[:]
		flag = 1
		#QL
		for i in range(self.size) :
			if flag != 1:
				break
			for j in range(self.size) :
				if not copy[i][j] :
					flag +=1
					break
		#DL
		for i in range(self.size) :
			if flag != 2:
				break
			for j in range(i+1) :
				if i == j :
					continue
				if not (copy[i][j] or copy[j][i]) :
					flag += 1
					break
		#RL
		for i in range(self.size) :
			for j in range(i+1):
				if copy[i][j] or copy[j][i] :
					copy[i][j]=copy[j][i]=1
		for i in range(self.size) :
			if flag != 3:
				break
			for j in range(self.size) :
				if i == j :
					continue
				if not copy[i][j] :

					flag +=1
					break

		self.judge = flag

	def mainloop(self):
		duty.userinput()
		duty.warshall()
		duty.judugGrap()
		print self.graType[self.judge]

duty = Graphics()
duty.mainloop()