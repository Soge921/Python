import random

dizionario = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"} 
mac = []
def genera():
    for _ in range (17):
         a=random.randint(0,15)
         mac.append(dizionario[a])
    for j in range(2,17,3):
        mac[j]=":"
    print(mac)
genera()