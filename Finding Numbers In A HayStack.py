#import regular expressions
import re

numlist = list() #Create a list to store numerical values
def sum_of_text(file_2_read):
	txt_2_sort = open(file_2_read, 'r') #Read the data file
	
	for line in txt_2_sort:
		line = line.rstrip() #Remove white space
		stuff = re.findall('[0-9]+', line) #Finding all numberical values
		if len(stuff) == 0: continue #Excludes all blank/NA values
		for x in stuff:
			numlist.append(int(x)) #Appends all numerical values to the numlist list

	print len(numlist) #prints the number of elements in the list 
	print sum(numlist) #prints the sum of the list


#Runs the function 		
sum_of_text('Actual data.txt') 



