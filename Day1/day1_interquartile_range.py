def find_median(array, length):
	#median
	mid_point = int(length/2)
	if length%2==0:
	    median = (array[mid_point]+array[ mid_point-1])/2
	else:
	    median = array[mid_point]
	return median

length = int(input())
value = list(map(int, str(input()).split(' ')))
frequency = list(map(int, str(input()).split(' ')))

array = []
for i in range(length):
	elem = value[i]
	for j in range(frequency[i]):
		array.append(elem)

import pdb; pdb.set_trace()
array.sort()
#updating the length to the new set length
length = len(array)
#Divide the array into two halves
mid_point = int(length/2)
if length%2 == 0:
	lower = array[:mid_point]
	upper = array[mid_point:]
else:
	lower = array[:mid_point]
	upper = array[mid_point+1:]

first_quartile = find_median(lower, len(lower))
third_quartile = find_median(upper, len(upper))

inter_quartile_range = third_quartile - first_quartile

print("{:.1f}".format(inter_quartile_range))