list1 = [[1,0.25],[2,0.40],[3,0.20],[4,0.15]]
list2 = [[2,0.30],[3,0.28],[4,0.25],[5,0.17]]
list3 = [[3,0.35],[4,0.25],[5,0.20],[6,0.20]]
R_D_Arr = [0,26,98,90,26,42]
R_D_Ser = [95,21,51,92,38,43]
def sumtotal(list1):
	n = 0
	for i in list1:
		n += i[1]
	#print n

def space(z):
	return z+(15-len(z))*" "

def write(list1):
	for i in list1:
		for j in i:
			print space(str(j)),
		print space("|")
def cum_prob(list1):
	cumu = 0
	x = 0
	for i in list1:
		cumu += i[1]
		i.append(cumu)
		i.append([int(x*100),int((cumu*100)-1)])
		x = cumu
	print space("I.A.T."),space("Prob"),space("Cummu_prob"),space("Range")
	print "--------------------------------------------------------------"
	write(list1)
print "----Arrival_Table----"
cum_prob(list1)
print "----Able_Table----"
cum_prob(list2)
print "----Banker_Table----"
cum_prob(list3)

print "Random digit for Arrival =",R_D_Arr
print "Random digit for Ser =",R_D_Ser
print "\n"+("Cust_no"),("I.A.T."),("A.T."),("|"),("S.T."),("S.B."),("S.E."),("|"),("S.T."),(" S.B."),("S.E."),("|"),("Time_in_sys ")
print "------------------------------------------------------------------------------------------"
def inti_Arr(n,m):
	for i in m:
		if i[3][0]<n:
			if i[3][1] >= n:
				return i[0]
		else:
			return 0
def ser1(n,m,o,p,st,a1,se):
	sb = a1
	arr = []
	arr1 = []
	arr2 = []
	if se > a1:
		st = inti_Arr(n,o)
		sb = a1
		se = int(st+a1)
		arr1 =[st,sb,se]
		#arr1.append(arr2)
		#comp(arr2,a1)
		return arr1
	
	else :
		st = inti_Arr(n,m)
		sb = a1
		se = int(st+a1)
		arr2 =[st,sb,se]

		#arr2 = comp(arr2,a1)
		#arr1.append(arr2)
		return arr2

def comp(arr2,a1):
	if arr2[-1] > a1:
		arr2 = (arr2[0],arr2[1],arr2[2])
		return arr2
	else:
		arr2 = (arr2[0],arr2[1],arr2[2])
		return arr2

def comp_part(list1,list2,list3):
	cust = 0
	a1 = 0
	b1 = 0
	arr = []
	spc = "   "
	st = 0
	find_Able = [0,0,0]
	array = []
	se = 0
	for i in range(1,7):
		st = find_Able[0]
		se = find_Able[2]
		find_Arr = inti_Arr(R_D_Arr[i-1],list1)
		a1+=find_Arr
		cust+=1
		find_Able = ser1(R_D_Ser[i-1],list2,list3,find_Arr,st,a1,se)
		#print find_Able
		arr.append([cust,find_Arr,a1,find_Able[0],find_Able[1],find_Able[2]])
	arr1 = []
	for i in range(0,5):

		for j in range(0,5):
			x = arr[i][5],arr[i+1][2]
			#print x
		if arr[i][5] > arr[i+1][2]:
			print "\n",arr[i][0],spc,arr[i][1],spc,arr[i][2],spc,arr[i][3],spc,arr[i][4],spc,arr[i][5],spc,0,spc,0,spc,0,spc,arr[i][3]
			arr1.append([arr[i+1][0],arr[i][5]])
			#print arr1
		else:
			print "\n",arr[i][0],spc,arr[i][1],spc,arr[i][2],spc,0,spc,0,spc,0,spc,arr[i][3],spc,arr[i][4],spc,arr[i][5],spc,arr[i][3]
			arr1.append([arr[i+1][0],arr[i][5]])
			#print arr1
			#if arr[i+1][2] > arr[i][5]:
				#print arr

		#print "\n",cust,spc,find_Arr,spc,a1,spc,find_Able[0],spc,find_Able[1],spc,find_Able[2],spc,0,spc,0,spc,0,spc,find_Able[0]
		#print "\n",(cust),spc,(find_Arr),spc,(a1),spc,(find_Able[0]),spc,(find_Able[1]),spc,(find_Able[2]),spc,(find_Able[3]),spc,(find_Able[4]),spc,(find_Able[5]),spc,(find_Able[6])
		#print arr1
		#array.append([(cust),(find_Arr),(a1),(find_Able[0]),(find_Able[1]),(find_Able[2]),(find_Able[3]),(find_Able[4]),(find_Able[5]),(find_Able[6])])
		#print find_Able
		#array.append([cust,find_Arr,a1,find_Able[0],find_Able[1],find_Able[2]])
#	print array
#	for i in range(0,5):
#		for j in range(0,6):
#
#			print array[i][5],array[i+1][2]
#			#if array[i+1][i+2]<=array[i][i+5]:
#
	#print array[0]
comp_part(list1,list2,list3)

