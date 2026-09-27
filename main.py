import turtle
import time
import random


WIDTH = 500
HEIGHT = 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'white', 'brown', 'purple', 'pink', 'black']


def get_number_of_racers():
    while True:
        racers = input("Введите кол-во черепеах для гонки от 2 до 10: ")

        if not racers.isdigit():
            print("Вы ввели не число, попробуйте еще раз")
            continue

        racers = int(racers)

        if racers < 2 or racers > 10:
            print("Число черепах должно быть от 2 до 10")
            continue

        return racers


def init_turtle():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Гонки черепах")
    time.sleep(10)


def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(COLORS) + 1)
    for number, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup() 
        x = -WIDTH / 2 + (number + 1) * spacing
        y = -HEIGHT / 2 + 20
        racer.setpos(x, y)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return racer.color()[0]


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
turtles = create_turtles(colors)
winner = race(turtles)
print(f"Победила черепашка {winner} цвета")
turtle.done()