def mean(numlist):
    sum = 0
    for num in numlist:
        sum = sum + num
    return sum / len(numlist)

def mode(numlist):
    ctr = 0
    num = numlist[0]

    for i in numlist:
        freq = numlist.count(i)
        if(freq > ctr):
            ctr = freq
            num = i
        if len(set(numlist)) == len(numlist):
            return 'There is no mode for the list.'   
    return num

def median(numlist):
    numlist.sort()
    if len(numlist) % 2 != 0:
        midloc = int((len(numlist)-1)/2)
        return numlist[midloc]
    elif len(numlist) % 2 == 0:
        mid1 = int((len(numlist))/2)
        mid2 = int((len(numlist))/2) - 1
        return int(mean(numlist[mid1],numlist[mid2]))

user_list = []

while(True):
    prompt =  input('Enter a number and input UWU to calculate:')
    if prompt == 'UWU':
        break
    user_list.append(int(prompt))

mean = str(mean(user_list))
mode = str(mode(user_list))
median = str(median(user_list))

print('Mean: ' + mean + '\n' + 'Median: ' + median + '\n' + 'Mode: ' + mode)
