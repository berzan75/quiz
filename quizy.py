import pgzrun

WIDTH= 870
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







pgzrun.go()

