import turtle

def meter(fill_amount):
    global turtle2, turtle2_start
    turtle2.hideturtle()
    turtle2.pencolor("black")
    turtle2.goto(turtle2_start)
    turtle2.penup()
    turtle2.speed(50)
    turtle2.goto(-300, 150)
    turtle2.pendown()
    turtle2.width(7)
    turtle2.left(90)
    turtle2.circle(45, 180)  
    turtle2.forward(300)  
    x2, y2 = turtle2.pos()
    turtle2.circle(45, 180)
    turtle2.forward(300)
    turtle2.penup()
    turtle2.goto(x2+1, y2+4)
    turtle2.left(180)
    turtle2.circle(45, 90)
    turtle2.left(90)
    turtle2.width(84)
    turtle2.speed(1)
    turtle2.forward(40)
    turtle2.pendown()
    turtle2.pencolor("red")
    turtle2.forward((fill_amount / 100) * 300)
    turtle2.speed(50)
    turtle2.penup()
    turtle2.goto(0,0)
    turtle2.right(90)

def display_question():
    screen.tracer(False)
    turtle1.hideturtle()
    turtle1.clear()
    turtle1.penup()
    turtle1.goto(-160, 135)
    turtle1.width(1)
    turtle1.pendown()
    turtle1.fillcolor("lightblue")
    turtle1.begin_fill()
    turtle1.forward(600 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(60 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(600 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(60 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.penup()
    turtle1.end_fill()
    turtle1.goto(-155, 150)
    turtle1.pendown()
    questions_text = questions[current_question]
    max_line_length = 70
    lines = [questions_text[i:i+max_line_length] for i in range (0, len(questions_text), max_line_length)]
    formatted_question = '\n'.join(lines)

    turtle1.write(formatted_question, align = "left", font=("Arial", 14, "normal"))

    for i, answer in enumerate(answers[current_question]):
        rectangle(-160, 30 - i * 100)
        turtle1.penup()
        turtle1.goto(-140, 80 - i * 100)
        turtle1.pendown()
        turtle1.write(f"{chr(65 +i)}. {answer}", font = ("Arial", 12, "normal"))
        if current_question <= 2:
            screen.bgpic("room.gif")
        elif current_question <= 6:
            screen.bgpic("campus.gif")
    screen.tracer(True)

def rectangle(x, y):
    turtle1.hideturtle()
    screen.tracer(False)
    turtle1.penup()
    turtle1.goto(x, y)
    turtle1.pencolor("black")
    turtle1.width(1)
    turtle1.pendown()
    turtle1.fillcolor("lightblue")
    turtle1.begin_fill()
    turtle1.forward(600 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(80 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(600 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.forward(80 - 2 * 10)
    turtle1.circle(10, 90)
    turtle1.end_fill()
    screen.tracer(True)

def check_choice(x, y):
    global answer_choice, wrong_score, score
    for i in range(len(answers[current_question])):
        x1 = -160
        y1 = 0 - i * 100
        x2 = 340
        y2 = y1 + 80
        if x1 <= x <= x2 and y1 <= y <= y2:
            answer_choice = i
            if answer_choice == correct_answers[current_question]:
                score += weight[current_question]
            else:
                score -= weight[current_question]
                wrong_score += weight[current_question]
            next_question()
            return
            
def next_question():
    global current_question, answer_choice, wrong_score
    current_question += 1
    answer_choice = None
    screen.onscreenclick(None)
    if current_question < len(questions):
        display_question()
        screen.onscreenclick(check_choice)
        turtle1.penup()
        meter(wrong_score)
    elif current_question == len(questions):
        if score >= 25:
            turtle1.clear()
            turtle2.clear()
            turtle1.goto(-180, 200)
            turtle1.write(f"Congradulations! YOU GRADUATED", font = ("Arial", 20, "normal"))
            screen.bgpic("graduated.gif")
        elif score > -35:
            turtle1.clear()
            turtle2.clear()
            turtle1.goto(-390, 250)
            turtle1.write(f"You made some poor decisions, you need an extra semester to graduate.", font = ("Arial", 20, "normal"))
            screen.bgpic("failed.gif")
        else:
            turtle1.clear()
            turtle2.clear()
            turtle1.goto(-370, 250)
            turtle1.write(f"You made many poor decisions, you need to take a few extra semesters to graduate.", font = ("Arial", 15, "normal"))
            screen.bgpic("stressed.gif")
    else:
        turtle.bye()

def start_screen():
    turtle1.hideturtle()
    turtle2.hideturtle()
    turtle1.penup()
    turtle2.penup()
    turtle1.clear()
    turtle2.clear()
    turtle1.goto(-220,200)
    turtle1.pencolor("white")
    turtle1.write("Welcome to the graduation game!", font = ("Ariel", 16, "bold"))
    turtle1.goto(-466, 150)
    turtle1.write("Answer your best and see if you know how to manage your time to graduate!", font = ("Ariel", 16, "bold"))
    turtle1.pencolor("maroon")
    turtle1.goto(-580, 100)
    turtle1.write("The stress meter will let you know how your doing, the higher the meter the more stressed you are.", font = ("Ariel", 15, "bold"))
    turtle1.goto(-155, 50)
    turtle1.write("Click anywhere to start!", font = ("Ariel", 15, "bold"))
    turtle1.pencolor("black")
    screen.onscreenclick(start_game)

def start_game(x, y):
    screen.onscreenclick(None)
    turtle1.clear()
    display_question()
    screen.onscreenclick(check_choice)
    turtle1.penup()
    meter(wrong_score)

# Setup
screen = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
screen.bgcolor("lightblue")
screen.setup(width = 1280, height = 720)
turtle1.speed(10)

# Ansewers and questions 
contents = open("QandA.txt")
lines = contents.readlines()
questions = []
answers = []
both_answers = []
correct_answers = []
weight = []

for i in range(len(lines)):
    questions.append(lines[i].split(',')[0])
    both_answers = lines[i].split(',')[1]+';'+lines[i].split(',')[2]
    list_answers = [answers.strip() for answers in both_answers.split(';')]
    correct_answers.append(int(lines[i].split(',')[3].strip()))
    answers.append(list_answers)
    weight.append(int(lines[i].split(',')[4]))

global score
global wrong_score
global turtle2_start
turtle2_start = turtle2.pos()
wrong_score = 0
score = 0
current_question = 0
answer_choice = []
start_screen()

turtle.mainloop()