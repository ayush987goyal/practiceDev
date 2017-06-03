mainList = [[" "," "," "],[" "," "," "],[" "," "," "]]
index = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def printMain(l):
	for [l1,l2,l3] in l:
		print("-------------")
		print ("| " +l1 + " | "+ l2+" | "+ l3+" |")

	print("-------------")

def valueGetter(loc):
	global mainList,index
	return mainList[index[loc][0]][index[loc][1]]
	
def query(p1,p2,p3):
	if(valueGetter(p1)==valueGetter(p2) and valueGetter(p1)==valueGetter(p3) and valueGetter(p1)!=" "):
		return True
	else:
		return False

def successCheck(testList):
	if(query(0,1,2) or query(3,4,5) or query(6,7,8) or query(0,3,6) or query(1,4,7) or query(2,5,8) or query(0,4,8) or query(2,4,6)):
		return True
	else:
		return False

count=1

print("Tic Tac Toe!")
printMain(mainList)

while(successCheck(mainList)!=True):
	response = input("Enter your choice(1-9): ")
	if(count%2 != 0):
		if(mainList[index[response-1][0]][index[response-1][1]]==" "):
			mainList[index[response-1][0]][index[response-1][1]] = "x"
		else:
			print("Wrong choice! Try again")
			continue
		count+=1
	else:
		if(mainList[index[response-1][0]][index[response-1][1]]==" "):
			mainList[index[response-1][0]][index[response-1][1]] = "o"
		else:
			print("Wrong choice! Try again")
			continue
		count+=1
	printMain(mainList)

printMain(mainList)

if(count==10):
	print("Draw!")
elif(count%2 == 0):
	print("Winner is : x")
else:
	print("Winner is : o")	
	
