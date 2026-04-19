import turtle
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.title("Turtle Race with History Chart")
screen.setup(width=1000, height=700)
screen.bgcolor("white")

# ---------------- DATA ----------------
colors = ["blue", "red", "pink"]
start_positions = [120, 40, -40]
racers = []
winner_history = []
race_running = False

finish_x = 250

# ---------------- DRAWERS ----------------
line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.penup()

message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.penup()

chart_writer = turtle.Turtle()
chart_writer.hideturtle()
chart_writer.penup()

button_drawer = turtle.Turtle()
button_drawer.hideturtle()
button_drawer.penup()

# ---------------- CREATE RACERS ----------------
for i in range(3):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-350, start_positions[i])
    racers.append(racer)

# ---------------- FINISH LINE ----------------

def draw_square(drawer, x, y, size, color):
    drawer.goto(x, y)
    drawer.setheading(0)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()

    for _ in range(4):
        drawer.forward(size)
        drawer.right(90)

    drawer.end_fill()
    drawer.penup()

def draw_finish_line():
    line_drawer.clear()

    # pole
    line_drawer.goto(finish_x - 10, 180)
    line_drawer.setheading(-90)
    line_drawer.pensize(4)
    line_drawer.pendown()
    line_drawer.forward(360)
    line_drawer.penup()
    line_drawer.pensize(1)

    # checkered flag
    start_x = finish_x
    start_y = 180
    square_size = 20
    rows = 18
    cols = 4

    for row in range(rows):
        for col in range(cols):
            x = start_x + (col * square_size)
            y = start_y - (row * square_size)

            if (row + col) % 2 == 0:
                color = "black"
            else:
                color = "white"

            draw_square(line_drawer, x, y, square_size, color)

    # outline around flag
    line_drawer.goto(start_x, start_y)
    line_drawer.setheading(0)
    line_drawer.pendown()
    for _ in range(2):
        line_drawer.forward(cols * square_size)
        line_drawer.right(90)
        line_drawer.forward(rows * square_size)
        line_drawer.right(90)
    line_drawer.penup()


# ---------------- START BUTTON ----------------
def draw_start_button():
    button_drawer.clear()
    button_drawer.goto(-80, -280)
    button_drawer.setheading(0)
    button_drawer.pendown()

    for _ in range(2):
        button_drawer.forward(160)
        button_drawer.left(90)
        button_drawer.forward(50)
        button_drawer.left(90)

    button_drawer.penup()
    button_drawer.goto(-38, -265)
    button_drawer.write("START", font=("Arial", 16, "bold"))

# ---------------- RESET RACERS ----------------
def reset_racers():
    for i in range(3):
        racers[i].goto(-350, start_positions[i])

# ---------------- HISTORY CHART ----------------
def draw_history_chart():
    chart_writer.clear()

    chart_writer.goto(420, 260)
    chart_writer.write("Winner History", font=("Arial", 16, "bold"))

    if len(winner_history) == 0:
        return

    start_x = 420
    start_y = 220
    row_spacing = 28
    col_spacing = 28
    max_rows = 6

    x = start_x
    y = start_y

    current_column = 0
    current_row = 0

    previous_winner = winner_history[0]

    chart_writer.goto(x, y)
    chart_writer.dot(20, previous_winner)

    for i in range(1, len(winner_history)):
        current_winner = winner_history[i]

        if current_winner == previous_winner and current_row < max_rows - 1:
            current_row += 1
        else:
            current_column += 1
            current_row = 0

        x = start_x + (current_column * col_spacing)
        y = start_y - (current_row * row_spacing)

        chart_writer.goto(x, y)
        chart_writer.dot(20, current_winner)

        previous_winner = current_winner

# ---------------- MESSAGE ----------------
def show_message(text):
    message_writer.clear()
    message_writer.goto(-120, 250)
    message_writer.write(text, font=("Arial", 18, "bold"))

# ---------------- RACE ----------------
def race():
    global race_running

    if race_running:
        return

    race_running = True
    show_message("Race started...")
    reset_racers()

    winner = None

    while winner is None:
        for racer in racers:
            move_amount = random.randint(1, 10)
            racer.forward(move_amount)

            if racer.xcor() >= finish_x:
                winner = racer.pencolor()
                break

    winner_history.append(winner)
    show_message(winner.upper() + " Congraulations!")
    draw_history_chart()

    race_running = False

# ---------------- CLICK HANDLER ----------------
def click_handler(x, y):
    if -80 <= x <= 80 and -280 <= y <= -230:
        race()

# ---------------- SETUP ----------------
draw_finish_line()
draw_start_button()
draw_history_chart()

screen.onclick(click_handler)
screen.mainloop()




turtle.done()






