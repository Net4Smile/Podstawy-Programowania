def f(n: int):
  primeNumbers = []
  i = 2

  while len(primeNumbers) < n:
      isPrime = True
      for j in range(2, int(i ** 0.5) + 1):
          if i % j == 0:
              isPrime = False
              break
      if isPrime:
          primeNumbers.append(i)
      i += 1

  return primeNumbers[n - 1]

print(f(1))
print(f(5))