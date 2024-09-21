import random
import pgzrun

TITLE = "QuizMaster"
WIDTH = 870
HEIGHT = 650

marquee_Box = Rect(0, 0, 880, 80)
question_Box = Rect(0, 0, 650, 150)
timer_Box = Rect(0,0,150,150)
answer_Box1 = Rect(0, 0, 300, 150)
answer_Box2 = Rect(0, 0, 300, 150)
answer_Box3 = Rect(0, 0, 300, 150)
answer_Box4 = Rect(0, 0, 300, 150)
skip_Box = Rect(0, 0, 150, 330)

score = 0
time_Left = 10
question_File = "questions.txt"
marquee_Text = " "
is_Game_Over = False

answer_Boxes = [answer_Box1, answer_Box2, answer_Box3, answer_Box4]

questions = []
question_Count = 0
question_Index = 0

marquee_Box.move_ip(0,0)
question_Box.move_ip(20,100)
timer_Box.move_ip(700,100)
answer_Box1.move_ip(20,270)
answer_Box2.move_ip(370,270)
answer_Box3.move_ip(20,450)
answer_Box4.move_ip(370,450)
skip_Box.move_ip(700,270)


def draw():
    global marquee_Text, question_Index, question_Count
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_Box, "black")
    screen.draw.filled_rect(question_Box, "navy blue")
    screen.draw.filled_rect(timer_Box, "navy blue")
    screen.draw.filled_rect(skip_Box, "dark green")

    for i in answer_Boxes:
        screen.draw.filled_rect(i, "orange")
    
    marquee_Text = "WELCOME TO QUIZ MASTER"
    marquee_Text = marquee_Text + f"Q:{question_Index}of{question_Count}"

pgzrun.go()