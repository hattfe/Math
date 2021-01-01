import turtle
t = turtle.Pen()
t.speed(10)
x1 = []
y1 = []
for i in range(0, 36):
    t.circle(200,10)
    x, y =(t.pos())
    x1.append(int(x))
    y1.append(int(y))
        
print(x1, y1)
x11 = x1[0]
y11 = y1[0]
def basagit(node, adım):
    t.penup()
    t.goto(x1[node],y1[node])
    t.pendown()
    t.goto(x1[node+node*adım], y1[node+node*adım])
    

for n in range(len(x1)):
    basagit(n,2)
    
           
    
