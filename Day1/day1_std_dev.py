length = int(input())
array = list(map(int, str(input()).split(' ')))

#mean
mean = sum(arrays)/length

#Calculate the variance
variance = 0
for arr in arrays:
	variance+=pow(arr-mean, 2)
variance/=length

std_dev = pow(variance, 0.5)

print("{:.1f}".format(std_dev))