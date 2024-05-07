import turtle as t
t.begin_fill()
x,y=0,0
t.color("red","green")
def square(x,y):
  for i in range(4):
   t.fd(100)
   t.lt(90)
t.onclick(square)
t.end_fill()
t.done()
   
