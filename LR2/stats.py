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
        return int((numlist[mid1] + numlist[mid2])/2)

def checkempty(numlist):
    if len(numlist) == 0:
        return 0

def main(numlist):
    user_list = [7,7,3,9,11,23]

    meanlist = str(mean(user_list))
    modelist = str(mode(user_list))
    medianlist = str(median(user_list))
    
    print('Mean: ' + meanlist + '\n' + 'Median: ' + medianlist + '\n' + 'Mode: ' + modelist)

user_list = [7,7,3,9,11,23]
main(user_list)
