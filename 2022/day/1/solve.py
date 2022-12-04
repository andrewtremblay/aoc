def inputToArray():
    f = open('input.txt')
    lines = f.readlines()
    numbers = []
    for l in lines:
        num_check = l.replace("\n", "")
        if num_check != "":
            numbers.append(int(num_check))
        else:
            numbers.append(None)
    return numbers

def findSums(numbersArray):
    sums = []
    sum = 0
    for n in numbersArray:
        if n is None:
            sums.append(sum)
            sum = 0
        else:
            sum = sum + n
    return sums    

def day1():
    numbers = inputToArray()
    sums = findSums(numbers)
    sums.sort(reverse=True)
    max = sums[0]
    # part 1
    print(max)
    # part 2
    lastMax = sums[1]
    lastLastMax = sums[2]
    print(max + lastMax + lastLastMax)



day1()