import turtle 
import time 
import random 
  
delay = 0.1




win = turtle.Screen() 
win.title("il giuoco del serpentello") 
win.bgcolor("red") 
win.setup(width=600, height=600) 
win.tracer(0) 
   
testa = turtle.Turtle() 
testa.shape("circle") 
testa.color("green") 
testa.penup() 
testa.goto(0, 0) 
testa.direction = "Stop"
  
mela = turtle.Turtle() 
mela.speed(0) 
mela.shape("square") 
mela.color("blue") 
mela.penup() 
mela.goto(0, 120) 
  
def up(): 
    if testa.direction != "down": 
        testa.direction = "up"
  
  
def down(): 
    if testa.direction != "up": 
        testa.direction = "down"
  
  
def left(): 
    if testa.direction != "right": 
        testa.direction = "left"
  
  
def right(): 
    if testa.direction != "left": 
        testa.direction = "right"
  
  
def move(): 
    if testa.direction == "up": 
        y = testa.ycor() 
        testa.sety(y+20) 
    if testa.direction == "down": 
        y = testa.ycor() 
        testa.sety(y-20) 
    if testa.direction == "left": 
        x = testa.xcor() 
        testa.setx(x-20) 
    if testa.direction == "right": 
        x = testa.xcor() 
        testa.setx(x+20) 
  
  
          
win.listen() 
win.onkeypress(up, "w") 
win.onkeypress(down, "s") 
win.onkeypress(left, "a") 
win.onkeypress(right, "d") 
  
coda = [] 
  
  
  

while True: 
    win.update() 
    if testa.xcor() > 290 or testa.xcor() < -290 or testa.ycor() > 290 or testa.ycor() < -290: 
        time.sleep(1) 
        testa.goto(0, 0) 
        testa.direction = "Stop"
        for ind in range(0,len(coda)): 
            coda[ind].goto(610, 610) 
        coda.clear() 
       
        
    if testa.distance(mela) < 20: 
        x = random.randint(-270, 270) 
        y = random.randint(-270, 270) 
        mela.goto(x, y) 
  
       
        new_block = turtle.Turtle() 
        new_block.speed(0) 
        new_block.shape("circle") 
        new_block.color("yellow")  
        new_block.penup() 
        coda.append(new_block) 
        
        
    
    for index in range(len(coda)-1, 0, -1): 
        x = coda[index-1].xcor() 
        y = coda[index-1].ycor() 
        coda[index].goto(x, y) 
    if len(coda) > 0: 
        x = testa.xcor() 
        y = testa.ycor() 
        coda[0].goto(x, y) 
    move() 
    for segment in coda: 
        if segment.distance(testa) < 15: 
            time.sleep(1) 
            testa.goto(0, 0) 
            testa.direction = "stop"
            for ind in range(0,len(coda)): 
                coda[ind].goto(610, 610) 
            coda.clear() 
            
         
    time.sleep(delay) 
  
win.mainloop()