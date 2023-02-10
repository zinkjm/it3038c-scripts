
print('Enter a number and I\'ll tell you how many prime number are between it and 0')
yourNumber = int(input())

# Assigning a number for testing if it's a prime number
testPrime = 0
# Variable to count the nonPrime numbers 
nonPrimeNumber = 0
# Variable to assign the prime numbers
primeNumbers = 0

# will loop the iterations until hitting the entered number
while testPrime < yourNumber:
	# Variable to test if a number is divisible and not prime. Must be 2 because prime numbers can be divided by 1
	divisor = 2

	# 0 and 1 will never be prime
	if testPrime == 0 or testPrime == 1:
		nonPrimeNumber = nonPrimeNumber + 1

	else:
		# Will loop through all the possible divisors to see if the testPrime is a prime number
		while divisor < testPrime:
			# This tests if the test number can be divided by any number less than it
			if (testPrime % divisor) == 0:
				# If the testPrime can be divided then it's not prime, will be counted and go to the next number to test
				nonPrimeNumber = nonPrimeNumber + 1
				break 
			divisor = divisor + 1

	testPrime = testPrime + 1

# Find the prime numbers
primeNumbers = yourNumber - nonPrimeNumber

print('There are %s prime numbers between 0 and %s' % (primeNumbers, yourNumber))
	