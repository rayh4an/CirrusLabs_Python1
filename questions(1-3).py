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

def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n)

print('The number [523] converted to words is ' + str(number_to_words(523)))

print('\nQuestion 3\n')

def ticTacToe(board):
    for i in range(len(board)):
        print(" | ".join(board[i]))
        if i < len(board) - 1:
            print("-" * 9)

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

ticTacToe(board)