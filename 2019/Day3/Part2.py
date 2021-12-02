rows, cols = (11000, 10000)
startrow = 3100
startcolumn = 2700
wirecount = 1

def getNewCellValue (currentValue, wirecount, stepCount):
	if wirecount == 1:
		if currentValue == 0:
			return stepCount
		elif currentValue == -1:
			return -1
		else:
			return currentValue
	else:
		if currentValue > 0:
			return currentValue + stepCount
		else:
			return 1000000000

#Intialize Array
arr =  [[0 for i in range(cols)] for j in range(rows)]

#Set Start
arr[startrow][startcolumn] = -1

input = open("directions.txt", "r")
wire = input.readline()
currentDistance = 1000000000

while wire:
#	print(wire)
	steps = wire.split(",")

	#Reset to beginning
	r = startrow
	c = startcolumn
	stepCount = 1

	for step in steps:
		print(step)
		direction = step[0]
		count = int(step[1:])
		if direction == "R":
			for column in range (c+1, c+count+1, 1):
				value = getNewCellValue(arr[r][column] ,wirecount, stepCount)
				if wirecount == 1:
					arr[r][column] = value
				else:
					if value < currentDistance:
						currentDistance = value
				stepCount += 1
			c = column
			print("row: " + str(r) + " col: " + str(c))
		elif direction == "L":
			for column in range (c-1, c-count-1, -1):
				value = getNewCellValue(arr[r][column] ,wirecount, stepCount)
				if wirecount == 1:
					arr[r][column] = value
				else:
					if value < currentDistance:
						currentDistance = value
				stepCount += 1
			c = column
			print("row: " + str(r) + " col: " + str(c))
		elif direction == "U":
			for row in range (r-1, r-count-1, -1):
				value = getNewCellValue(arr[row][c] ,wirecount, stepCount)
				if wirecount == 1:
					arr[row][c] = value
				else:
					if value < currentDistance:
						currentDistance = value
				stepCount += 1
			r = row
			print("row: " + str(r) + " col: " + str(c))
		else:
			for row in range (r+1, r+count+1, 1):
				value = getNewCellValue(arr[row][c] ,wirecount, stepCount)
				if wirecount == 1:
					arr[row][c] = value
				else:
					if value < currentDistance:
						currentDistance = value
				stepCount += 1
			r = row
			print("row: " + str(r) + " col: " + str(c))
	wirecount += 1
	wire = input.readline()
	
print(currentDistance)
