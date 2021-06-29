import turtle, random

border = turtle.Turtle()
window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

balls = []
count = 4
for i in range(count):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.up()
    randx = random.randint(-290,290)
    randy = random.randint(-290,290)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green,blue)
    ball.goto(randx,randy)
    dx = random.randint(-5,5)
    dy = random.randint(-5,5)
    balls.append([ball, dx, dy])

for i in balls:
    print(i)
while True:
    for i in range(count):
        balls[i]
            # balls[i][0] - мяч
            # balls[i][1] - dx
            # balls[i][2] - dy
        x,y = balls[i][0].position()
        if x+balls[i][1]>=300 or x+balls[i][1] <= -300:
            balls[i][1] = -balls[i][1]
        if y+balls[i][2]>=300 or y+balls[i][2] <= -300:
            balls[i][2] = -balls[i][2]
        balls[i][0].goto(x+balls[i][1], y+balls[i][2])

window.mainloop()


