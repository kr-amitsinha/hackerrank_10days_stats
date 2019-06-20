def find_median(array, length):
	#median
	mid_point = int(length/2)
	if length%2==0:
	    median = (array[mid_point]+array[ mid_point-1])/2
	else:
	    median = array[mid_point]
	return median

length = int(input())
array = list(map(int, str(input()).split(' ')))
array.sort()
#Divide the array into two halves
mid_point = int(length/2)
if length%2 == 0:
	lower = array[:mid_point]
	upper = array[mid_point:]
else:
	lower = array[:mid_point]
	upper = array[mid_point+1:]

first_quartile = find_median(lower, len(lower))
second_quartile = find_median(array, length)
third_quartile = find_median(upper, len(upper))

print(first_quartile)
print(second_quartile)
print(third_quartile)
