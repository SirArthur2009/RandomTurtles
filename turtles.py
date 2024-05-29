import turtle
import random

turtle.screensize(4000, 4000)

wn = turtle.Screen()

thurgan = turtle.Turtle()
logan = turtle.Turtle()

logan.speed(0)
thurgan.speed(0)

def pickRandomMove(lastMove):
    if lastMove in ["rt", "left"]:
        num = random.randint(0, 100)
        if num >= 0 and num < 40:
            return "fd"
        elif num >= 40 and num < 50:
            return "rt"
        elif num >= 50 and num < 60:
            return "left"
        elif num >= 60 and num <= 100:
            return "bk"
    else:
        num = random.randint(0, 120)
        if num >= 0 and num < 40:
            return "fd"
        elif num >= 40 and num < 70:
            return "rt"
        elif num >= 70 and num < 100:
            return "left"
        elif num >= 100 and num <= 120:
            return "bk"

def changeColor(myTurtle, colors):
    values = 0
    for i in colors:
        values += 1
    myTurtle.color(colors[random.randint(0, values-1)])

def changePenSize(myTurtle):
    myTurtle.pensize(random.randint(0, 10))

def changeBGColor(colors):
    values = 0
    for i in colors:
        values += 1
    wn.bgcolor(colors[random.randint(0, values-1)])

def main():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black', 'white', 
          'gray', 'cyan', 'magenta', 'lime', 'teal', 'lavender', 'maroon', 'navy', 'olive', 'azure', 
          'indigo', 'violet', 'gold', 'silver', 'rose', 'lightgreen', 'turquoise', 'skyblue', 'coral']


    lastMoveL = "N/A"
    lastMoveT = "N/A"
    for i in range(200):
        thurgansRandomMove = pickRandomMove(lastMoveT)
        logansRandomMove = pickRandomMove(lastMoveL)

        if i % 10 == 0:
            changeColor(thurgan, colors)
            changeColor(logan, colors)
        if i%20==0:
            changePenSize(thurgan)
            changePenSize(logan)
        if i%50==0:
            changeBGColor(colors)

        if thurgansRandomMove == "fd":
            thurgan.fd(random.randint(0, 100))
            lastMoveT = "fd"
        elif thurgansRandomMove == "rt":
            thurgan.rt(random.randint(0, 360))
            lastMoveT = "rt"
        elif thurgansRandomMove == "left":
            thurgan.lt(random.randint(0, 360))
            lastMoveT = "left"
        elif thurgansRandomMove == "bk":
            thurgan.bk(random.randint(0, 100))
            lastMoveT = "bk"
        
        if logansRandomMove == "fd":
            logan.fd(random.randint(0, 100))
            lastMoveL = "fd"
        elif logansRandomMove == "rt":
            logan.rt(random.randint(0, 360))
            lastMoveL = "rt"
        elif logansRandomMove == "left":
            thurgan.lt(random.randint(0, 360))
            lastMoveL = "left"
        elif logansRandomMove == "bk":
            logan.bk(random.randint(0, 100))
            lastMoveL = "bk"
    wn.mainloop()


if __name__ == "__main__":
    main()
    
