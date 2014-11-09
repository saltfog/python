
#Leap Year Function
#Year must be evenly divisible by 4 and 100 and 400 to be a leap year

def IsLeapYear(year):
   if((year % 4) == 0):
      if((year % 100) == 0):
         if( (year % 400) == 0):
            return 1
         else:
            return 0
      else:
         return 1
   return 0

n = 0
print "Enter Year: ",
n = input()
if( IsLeapYear(n) == 1):
   print n, "is a leap year"
else:
   print n, "is NOT a leap year"

n = r



