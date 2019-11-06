import turtle
import math
import random
#starting conditions
player = turtle.Turtle()
player.hideturtle()
player.penup()
player.shape("turtle")
player.setheading(90)
player.setpos(-200,0)
player.speed(1)
player.color("yellow")
canvas = turtle.Screen()
canvas.bgcolor("black")
canvas.title("gamescreen")
gameover = turtle.Turtle()
gameover.penup()
gameover.hideturtle()
gameover.color("red")
gameover.speed(0)
gameover.setpos(-150, 330)
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("blue")
scoreboard.penup()
scoreboard.setpos(-300,320)
#borders
box = turtle.Turtle()
box.speed(0)
box.hideturtle()
box.setheading(0)
box.color("blue")
box.pensize(3)
box.penup()
box.setpos(-300,-300)
for i in range(4):
    box.pendown()
    box.forward(600)
    box.left(90)
player.showturtle()
#movement
spd = 50
def playerup():
    player.sety(player.ycor()+ spd)
    if (player.ycor()+ spd) > 287:
        player.speed(0)
        player.sety(287)
        player.speed(1)
def playerdown():
    player.sety(player.ycor()- spd)
    if (player.ycor()+ spd) < -287:
        player.speed(0)
        player.sety(-287)
        player.speed(1)
turtle.listen()
gravity = 3
obsspd = 3
#collision
def hit(t1, t2):
              xdistance = t1.xcor()-t2.xcor()
              ydistance = t1.ycor()-t2.ycor()
              if (abs(xdistance) < 20) and (abs(ydistance) < 130):
               return True

              else:
                  return False
            

#obstacle list
number_obstacles = 2
obstacles = []
numberslistx = list(range(-100,280))
numberslisty = list(range(143,190))  

for i in range(number_obstacles):
    obstacles.append(turtle.Turtle())
for obstacle in obstacles:
    obstacle.hideturtle()
    obstacle.speed(0)
    obstacle.color("green")
    obstacle.penup()
    obstacle.shape("square")
    obstacle.turtlesize(12,3)
    xobs = random.choice(numberslistx)
    yobs = random.choice(numberslisty)
    obstacle.setposition(xobs,yobs)
    obstacle.showturtle()
#obstacle2 list
number_obstacles2 = 2
obstacles2 = []
numberslistx = list(range(-100,280))
numberslisty = list(range(160,190))           
for i in range (number_obstacles2):
    obstacles2.append(turtle.Turtle())
for obstacle2 in obstacles2:
    obstacle2.hideturtle()
    obstacle2.speed(0)
    obstacle2.color("green")
    obstacle2.penup()
    obstacle2.shape("square")
    xobs = random.choice(numberslistx)
    yobs = random.choice(numberslisty)
    obstacle2.turtlesize(12,3)
    obstacle2.setposition(xobs,-yobs)
    obstacle2.showturtle()
    if(obstacle.xcor()-obstacle2.xcor())> 10:
        obstacle.setposition(xobs,yobs)
        obstacle2.setposition(xobs,-yobs)
        

#border
def fall():
    if (player.ycor()< -300):
        return True
def ceiling():
    if (player.ycor() > 300):
        return True
colors = ["red", "green","yellow","blue","purple","pink"]
points = 1
while True:
    player.sety(player.ycor()-gravity)
    xresetpos = random.choice(range(230,300))
    yresetpos = random.choice(range(140,190))

    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor()-obsspd)
        if (obstacle.xcor()-obsspd) < -270:
            obstacle.hideturtle()
            obstacle.setx(xresetpos)
            obstacle.sety(yresetpos)
            obstacle.showturtle()
            obsspd+=1
            points += 1
            display = points
            scoreboard.clear()
            scoreboard.write(display)
            player.color(random.choice(colors))
            obstacle.color(random.choice(colors))
            
       
    for obstacle2 in obstacles2:
        obstacle2.setx(obstacle2.xcor()-(obsspd))
        if (obstacle2.xcor()-obsspd) < -270:
            obstacle2.hideturtle()                   
            obstacle2.setx(xresetpos)
            obstacle2.sety(-(int(yresetpos))-15)
            obstacle2.showturtle()
            player.color(random.choice(colors))
            obstacle2.color(random.choice(colors))
        if hit(player, obstacle):
            player.hideturtle()
            player.setpos(400,0)
            gameover.color("red")
            gameover.setpos(-150,-20)
            gameover.write("Game over",False,"left",("Arial",50,))
            gameover.setpos(-160,-200)
            gameover.write("Press x to play again",False,"left",("Arial",30,))
            break
        if hit(player, obstacle2):
            player.hideturtle()
            player.setpos(400,0)
            gameover.setpos(-150,-20)
            gameover.write("Game over",False,"left",("Arial",50,))
            gameover.setpos(-160,-200)
            gameover.write("Press x to play again",False,"left",("Arial",30,))
            break
       
    if fall():
        player.hideturtle()
        player.setpos(400,0)
        gameover.setpos(-150,-20)
        gameover.write("Game over",False,"left",("Arial",50,))
        gameover.setpos(-160,-200)
        gameover.write("Press x to play again",False,"left",("Arial",30,))
        break
    if ceiling():
        player.setycor(280)
    #if score(player,obstacle1):
     #   points += 1
     #   display = points
     #   scoreboard.clear()
      #  scoreboard.write(display)
    turtle.onkeypress(playerup, "space")
    #turtle.onkeypress(playerdown, "Down")
    #if player.xcor() is obstacle1.xcor():
     #   points += 1
     #   scoreboard.clear()
      #  scoreboard.write(points)

#balken stoppen niet als jij beweegt
      












                







































