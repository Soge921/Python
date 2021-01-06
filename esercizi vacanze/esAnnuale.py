dizionario = {}
def MaxMin(A1,A2):
    max = -1000
    min = 1000
    while A1<=A2:
        if dizionario[A1]>max:
            max = dizionario[A1]
        if dizionario[A1]<min:
            min = dizionario[A1]
        A1=A1+1
    krint("il Max e':", max ,"il Min e':", min)
def lettura(file):
    j=1
    k=1
    for linea in file:
        if k==0:
            if j==1:
                line = linea.split(',')
                key = int(line[1])
                val1 = float(line[2])
                j=2
            else:
                line = linea.split(',')
                val2 = float(line[2])
                media=(val1+val2)/2
                dizionario[key]=media
                j=1
        else:
            k=0
file = open("./annual.csv", "r")
lettura(file)
A1 = int(input("inserisci l'Anno 1: "))
A2 = int(input("inserisci l'Anno 2: "))
maxmin(A1,A2)       
            

