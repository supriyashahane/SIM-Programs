category = [["filling",20,30],["crown",45,30],["cleaning",25,30],["extracting",50,35],["checkup",20,20]]

def total(list1):
	sum1 = 0
	for i in list1:
		sum1 += i[2]
	return sum1
def space(l):
	return l+(15-len(l))*" "
def print1(list1):
	for i in list1:
		for j in i:
			print space(str(j)),
		print space("|")

def findCat(n,list1):
	for i in list1:
		if i[5][0]<=n:
			if i[5][1]>=n:
				return [i[0],i[1]]

def lastT(list1):
	t = 8.0
	to = 0
	x = 0
	y = 0
	for i in list1:
		i.append(t)
		t+=(float(i[4])/100)
		i.append(t)#serendtime_i[6]__
		if i[5]<=i[1]:
			i.append(0)#waiting_time
		else:
			i.append(float((i[5]-i[1])))#ideal_time
		#y +=(float(i[8]))
		if i[5]>i[1]:
			i.append(0)
		else:
			i.append(float((i[1]-i[5])))#waitng_time
		x+=(float(i[7]))
		if i[5] <= i[1]:
			i[5] = i[1]

	#print " ",(i[5]),(i[1]),(i[5]-i[1])
	print1(list1)
	print "Total Waiting time =",x
	print "average Waiting time = ",x/8

def mainTable(list1):
	randomNo=[51,40,22,83,40,21,34,75]
	mainT=[]
	time=8.0
	for i in range(1,9):
		cat = findCat(randomNo[i-1],list1)
		mainT.append([i,time,randomNo[i-1],cat[0],cat[1]])
		time+=0.30
	lastT(mainT)
def cummProb(list1):
	cumm = 0
	a = 0
	for i in list1:
		cumm+=i[3]
		i.append(cumm)
		i.append([int(a*100),int((cumm*100)-1)])
		a= cumm
	print space("category"),space("timeReq(min)"),space("NoOfPatient"),space("Prob"),space("CummProb"),space("Range")
	print "----------------------------------------------------------------------------------------------------------"
	print1(list1)
	print "\n"+space("PatNo"),space("arriPat"),space("randNo"),space("category"),space("serviceDur"),space("serStartTime"),space("serEndTime"),space("WTime"),space("Ideatim")
	print "-------------------------------------------------------------------------------------------------------------------------------------------------------"
	mainTable(list1)

def cal_prob(list1):
	totSum = total(list1)
	for i in list1:
		i.append(float(i[2])/totSum)
	cummProb(list1)
print cal_prob(category)
