import pgzrun

WIDTH= 840
HEIGHT= 600
TITLE="quiz"

marquee_box=Rect(0,10,880,80)
question_box=Rect(20,100,650, 150)
skip_box=Rect(700,270,150,330)
timer_box=Rect(700,100,150,150)
answer_box1=Rect(20,270,300,150)
answer_box2=Rect(370,270,300,150)
answer_box3=Rect(20,450,300,150)
answer_box4=Rect(370,450,300,150)

answerboxes=[answer_box1, answer_box2,answer_box3, answer_box4]
questions=[]
question_file_name="questions.txt"
score=0
time_left=10
marquee_message=""
question_count=0
question_index=0
is_game_over=False

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"yellow")
    screen.draw.filled_rect(skip_box,"green")
    screen.draw.filled_rect(timer_box,"red")
    for answerbox in answerboxes:
        screen.draw.filled_rect(answerbox,"yellow")

    marquee_message="Welcome to the game of the day.You are at"+f"Q:{question_index}of{question_count}"

    screen.draw.textbox(
        marquee_message,
        marquee_box,
        color="black"       
     )

    screen.draw.textbox(
        "skip",
        skip_box,
        angle=-90,
        color="black"
        )
    screen.draw.textbox(
        str(time_left),timer_box,
        timer_box,
        color="black",
        shadow=(0.5, 0.5),
        scolor="grey"
    )
    screen.draw.textbox(
        question[0].strip(),
        question_box,
        color="black",
    )
    index=1
    for i in answerboxes:
        screen.draw.textbox(question[index].strip(),
        i,
        color="black"
                            )
def move_marquee():
    marquee_box.x=marquee_box.x+1
    if marquee_box.left>WIDTH:
        marquee_box.right=0
def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file: 
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index=1
    for i in answerboxes:
        if i.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index=index+1
    
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left, questions
    score= score+1
    if questions:
        question=read_next_question()
        time_left= 10
    else:
        game_over()

def game_over():
    global score, time_left, is_game_over
    message=f"game over!\nYou Got{score} questions correct."
    question=[message,"-","-","-","-"]
    time_left=0
    is_game_over=True
def skip_question():
    global time_left,question
    if questions and not is_game_over:
        question=read_next_question()
        time_left=10
    else:
        game_over()
def update_time_left():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        game_over
read_question_file()
question=read_next_question()
clock.schedule_interval(update_time_left,1)





pgzrun.go()

