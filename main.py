#This program was written by Tafara Gwarada
#The program will remove all years from the car database
#The aim is to read the original file in read mode and get all the data.
#We then open the same file in write mode and write all the data to the file except for the data we dont want anymore ie years in this example
#Our test should return a text file with no years included.


# open file in read mode 
with open("car_exercises_3.txt", "r") as f: 
	
	# read data line by line 
	data = f.readlines() 
	
# open file in write mode 
with open("car_exercises_3.txt", "w") as f: 
	
	for line in data : 
		
		# condition for data to be deleted 
		if line.strip("\n") != "2006" and line.strip("\n") != "1998" and line.strip("\n") != "2015" :
			f.write(line) 
