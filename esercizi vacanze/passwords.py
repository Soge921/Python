import random
dizionario = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"q", 11: "w", 12:"e", 13:"r", 14:"t", 15:"y", 16:"u", 17:"i", 18:"o", 19:"p",
20:"a", 21:"s", 22:"d", 23:"f", 24:"g", 25:"h", 26:"j", 27:"k", 28:"l", 29:"z", 30:"x", 31:"c", 32:"v", 33:"b", 34:"n", 35:"m", 36:"_", 37:".", 38:"!", 39:"?", 40:"-"} 
password = []
def gen_pass(a):
    if int(a) == 1:
        for _ in range (8):
             n=random.randint(0,40)
             password.append(dizionario[n])
        print(password)
    else:
        for _ in range (20):
             n=random.randint(0,40)
             password.append(dizionario[n])
        print(password)
c=input("semplice o complicata? 1-semplice --- 2-complicata ")
gen_pass(c)
