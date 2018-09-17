
from math import sqrt

def getVariance(theMean,count,listSet=[]):
	total = 0

	for nums in listSet:
		nums = float(nums)
		total += ((nums - theMean)**2)
	variance = total/count
	variance = math.sqrt(variance)
	print("The standard deviation of this set is: ", variance);



def getMean(total,count):
	theMean = 0;
	theMean = total/count
	return theMean;


def addSet(count,listSet=[],):
	total = 0;
	for x in listSet:
		x = float(x);
		total += x
	themean = getMean(total, count);
	getVariance(themean,count,listSet)
	return;

def getInput():
	count = 0;
	listSet=[];
	flag = True;

	while flag != False:
		listSet.append(input(f"Enter count: {count} of data set: "));
		count +=1;
		check = input("Do you have more to add 'y/n':");
		if check == 'y':
			flag = True
		else:
			flag = False
			addSet(count,listSet);
			return;


def main():
	getInput()
	return;

main();