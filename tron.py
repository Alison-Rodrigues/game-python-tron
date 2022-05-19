from turtle import *

from freegames import square, vector

p1xy = vector(-200, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(200, 0)
p2aim = vector(-4, 0)
p2body = set()

p3xy = vector(0, 200)
p3aim = vector(0, -4)
p3body = set()


def inside(head):
    """Return True if head inside screen."""
    return -300 < head.x < 300 and -300 < head.y < 300


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    p3xy.move(p3aim)
    p3head = p3xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue and green wins!')
        return

    if not inside(p1head) or p1head in p3body:
        print('Player blue and green wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red and green wins!')
        return

    if not inside(p2head) or p2head in p3body:
        print('Player red and green wins!')
        return

    if not inside(p3head) or p3head in p1body:
        print('Player red and blue wins!')
        return

    if not inside(p3head) or p3head in p2body:
        print('Player red and blue wins!')
        return

    if not inside(p1head) or p1head in p1body:
        print('Player blue and green wins!')
        return

    if not inside(p2head) or p2head in p2body:
        print('Player red and green wins!')
        return

    if not inside(p3head) or p3head in p3body:
        print('Player red and blue wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)
    p3body.add(p3head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    square(p3xy.x, p3xy.y, 3, 'green')
    update()
    ontimer(draw, 20)


setup(600, 600, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 's')
onkey(lambda: p2aim.rotate(90), 'g')
onkey(lambda: p2aim.rotate(-90), 'h')
onkey(lambda: p3aim.rotate(90), '9')
onkey(lambda: p3aim.rotate(-90), '5')
draw()
done()

#teste
#criação do Player 3
#Colocou colisão entre todos os players
#Colisão no próprio player
#Ajuste de velocidade

