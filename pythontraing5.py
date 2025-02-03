import turtle

turtle.bgcolor ("black")
turtle.speed (10)
turtle.hideturtle ()

colors = ("pink", "green", "red")

for i in range(120):
        for c in colors:
            turtle.color(c)
            turtle.circle(200-1, 100)
            turtle.lt(90)
            turtle.circle(200-1, 100)
            turtle.rt(60)
            turtle.end_fill()

turtle.mainloop()            