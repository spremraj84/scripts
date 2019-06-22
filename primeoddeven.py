# Take an input from user and print "Way" if number is even, print "fair" if
# number is odd and print "Wayfair" if number is Prime
# Usage : python3 primeoddeven.py
#!/usr/bin/python3
import sys
# take an input from user
number = int(input("Enter an number: "))

isEven = False
isOdd = False
isPrime = False
# 2 is a prime number so print Wayfair directly
if(number == 2):
    isPrime = True
else:
    for i in range(2,number):
        if(i == 2 and number%2 == 0):
            isEven = True
        else:
            isOdd = True

        if ( number %i == 0):
            isPrime = False
            break
        else:
            isPrime = True

if(isPrime):
    print("Wayfair")
elif (isEven and not isPrime):
    print ("Way")
elif (isOdd and not isPrime):
    print ("fair")
