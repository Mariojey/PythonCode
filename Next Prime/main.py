def isPrime(a):
    for i in range(2, a):
        if a%i == 0:
            return False
    return True

num = int(input("Podaj liczbę: "))
i = num + 1
while isPrime(i) == False:
    i+=1
print(i)