class exper:
    def __init__(self):
        self.var = []
        self.value = [] # the map of input
        self.num = 0 
        self.allvar = [] # var set
        self.Identitylist = [] # identity list
        self.halfgroup = 0
        self.close = 0
        self.corporable = 0
        self.swappable = 0
        self.niyuan = 0

    def userinput(self):
        self.var = raw_input("Input the range of var \n").split(" ")
        for i in range(len(self.var)):
            tempin = raw_input().split(" ")
            self.allvar = self.allvar + tempin
            self.value.append(tempin)
        self.allvar = set(self.allvar)
        self.num = len(self.var)

    def ishalfgroup(self):
        if self.close and self.corporable :
            self.halfgroup = 1
            print "It's a halfgroup"
        else :
            print "It's not a halfgroup"

    def isIdentity(self):
        # not finish
        if not self.Identitylist :
            print "No Identity"
        else :
            print "There are %d Identity(s) : %s" % (len(self.Identitylist),tuple(self.Identitylist))

    def inverse(self):
        pass

    def debug(self):
        print self.var
        print self.value
        print self.allvar

    def checkFB(self):
        flag = 0
        for i in self.allvar:
            if i not in self.var:
                print "%s is not in G . Set is not close" % i 
                flag = 1
                break
        if flag == 0 :
            print "It's close"
            self.close = 1

    def findpos(self,word):
        for i in range(self.num):
            if self.var[i] == word :
                return i

    def checkJH(self):
        flag = 0 
        for i in range(self.num):
            for j in range(i,self.num):
                for k in range(j,self.num):
                    value1 = self.value[self.findpos(self.value[i][j])][k]
                    value2 = self.value[i][self.findpos(self.value[j][k])]
                    if value1 != value2:
                        print "(%s*%s)*%s != %s*(%s*%s) It's not corporable" % (self.var[i],self.var[j],self.var[k],self.var[i],self.var[j],self.var[k])
                        flag = 1
                        break
                if flag == 1 :   
                    break  
            if flag == 1 :
                break
        if flag == 0 :
            print "It's corporable"
            self.corporable = 1

    def checkEX(self):
        flag = 0
        for i in range(self.num):
            for j in range(i,self.num):
                if self.value[i][j] != self.value[j][i]:
                    flag = 1
                    print "%s*%s != %s*%s It's not swappable" % (self.value[i][j],self.value[j][i],self.value[j][i],self.value[i][j])
                    break
            if flag == 1 :
                break
        if flag == 0 :
            print "It's swappable"
            self.swappable = 1

    def checkDM(self):
        flag = 0 
        for i in range(self.num):
            if self.value[i][i] != self.var[i]:
                flag = 1
                print "%s * %s != %s it's not idempotent" % (self.var[i],self.var[i],self.var[i])
                break
        if flag == 0 :
            print "It's idempotent"    

    def check(self):
        self.checkFB()
        self.checkEX()
        self.checkDM()
        self.checkJH()
        self.ishalfgroup()
        self.isIdentity()

    def mainloop(self):
        self.userinput()
        self.check()

while (1) :
    process = exper()
    process.mainloop()