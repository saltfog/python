## take input and add to a list
numbers = []
while len(numbers) < 5:
    numbers.append(raw_input("Please enter a number"))
 
print numbers
## calculate mean
 
def calculate_mean(numbers):
    total = float(0)
    for n in numbers:
        total += int(n)
    return (total/len(numbers))
 
print calculate_mean(numbers)
 
## calculate mode
 
def calculate_mode(numbers):
    highcount = 0
    for n in numbers:
        if numbers.count(n) > numbers.count(highcount):
            highcount = n
        return highcount
 
print calculate_mode(numbers)
       
## calculate median
 
def median(numbers):
    sortednumbers = sorted(numbers)
   # print sortednumbers
    listlength = len(sortednumbers)
    if listlength == float(1):
        return sortednumbers[listlength-1]
    elif listlength % 2 != 0:
        return float(sortednumbers[listlength/2])
    else:
        return float(sortednumbers[listlength/2] + sortednumbers[(listlength/2)-1]) / 2.0
       
print median(numbers)
