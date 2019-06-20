#Taking the inputs
length = int(input())
value = list(map(int, str(input()).split(' ')))
weight = list(map(int, str(input()).split(' ')))

summation = 0
for i in range(0,length):
	summation+=value[i]*weight[i]

weighted_mean  = summation/sum(weight)

print("{:.1f}".format(weighted_mean))
