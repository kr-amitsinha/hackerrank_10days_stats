#Taking the inputs
length = int(input())
arrays = list(map(int, str(input()).split(' ')))

#Sort the array
arrays.sort()

#mean
mean = sum(arrays)/length

#median
mid_point = int(length/2)
if length%2==0:
    median = (arrays[mid_point]+arrays[ mid_point-1])/2
else:
    median = arrays[mid_point]

#mode
freq_dic = {}
maxi = -1
possible_modes = []
for num in arrays:
    if num not in freq_dic:
        freq_dic[num] = 0
    freq_dic[num]+=1
    if freq_dic[num]>=maxi:
        if freq_dic[num]==maxi:
            possible_modes.append(num)
        else:
            possible_modes = [num]
        maxi = freq_dic[num]


print(mean)
print("{:.1f}".format(median))
print(min(possible_modes))