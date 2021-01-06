def SerieFibonacci(x):
    if x <= 1:
        return x
    else:
        return SerieFibonacci(x-1) + SerieFibonacci(x-2)
k = int(input("quanti numeri della serie vuoi visualizzare?  "))
for n in range(1, k+1):
    print(SerieFibonacci(n))