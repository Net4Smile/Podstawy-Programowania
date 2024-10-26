primeNumbersToFind = int(input('Enter number of prime numbers to find: '))

primeNumbers = []
i = 2

while len(primeNumbers) < primeNumbersToFind:
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(i)
    i += 1

print(primeNumbers)