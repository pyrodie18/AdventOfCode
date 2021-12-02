rows, cols = (11000, 10000)
startrow = 3100
startcolumn = 2700
wirecount = 1

def getNewCellValue (currentValue, wirecount):
	if currentValue == 0:
		return wirecount
	elif  currentValue == wirecount:
		return wirecount
	elif currentValue == 99:
		return 99
	else:
		return 100

#Intialize Array
arr =  [[0 for i in range(cols)] for j in range(rows)]

#Set Start
arr[startrow][startcolumn] = 99

input = open("directions.txt", "r")
wire = input.readline()
while wire:
#	print(wire)
	steps = wire.split(",")

	#Reset to beginning
	r = startrow
	c = startcolumn

	for step in steps:
		print(step)
		direction = step[0]
		count = int(step[1:])
		if direction == "R":
			for column in range (c+1, c+count+1, 1):
				arr[r][column] = getNewCellValue(arr[r][column] ,wirecount)
			c = column
			print("row: " + str(r) + " col: " + str(c))
		elif direction == "L":
			for column in range (c-1, c-count-1, -1):
				arr[r][column] = getNewCellValue(arr[r][column] ,wirecount)
			c = column
			print("row: " + str(r) + " col: " + str(c))
		elif direction == "U":
			for row in range (r-1, r-count-1, -1):
				arr[row][c] = getNewCellValue(arr[row][c] ,wirecount)
			r = row
			print("row: " + str(r) + " col: " + str(c))
		else:
			for row in range (r+1, r+count+1, 1):
				arr[row][c] = getNewCellValue(arr[row][c] ,wirecount)
			r = row
			print("row: " + str(r) + " col: " + str(c))
	wirecount += 1
	wire = input.readline()
	
currentDistance = 1000000000

for r in range (0, rows):
	for c in range (0, cols):
		if arr[r][c] == 100:
			distance = abs(startrow - r) + abs(startcolumn - c)
			if distance < currentDistance:
				currentDistance = distance
			print(currentDistance)
