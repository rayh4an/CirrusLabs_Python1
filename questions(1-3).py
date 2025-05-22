import inflect
print('Question 1\n')

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

def outputPrimeNum(begin, end):
    primeNum = []
    for num in range(begin, end + 1):
        if prime(num):
            primeNum.append(num)
    return primeNum

print('Prime numbers between 1 - 25 are ' + str(outputPrimeNum(1, 25)))

print('\nQuestion 2\n')



print('\nQuestion 3\n')

