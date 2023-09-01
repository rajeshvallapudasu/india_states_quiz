import turtle
import random
import pandas
from tkinter import messagebox
screen=turtle.Screen()
screen.title("My Indian States game")
image="rajeshindia.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()
random.shuffle(states_list)
print(states_list)
guessed_states=[]
for state in states_list:
    new_state = data[data["state"] == state]
    new_x=new_state.x
    new_y=new_state.y
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(float(new_x),float(new_y))
    t.write(new_state.no.item(),font=("ariel",10,"bold"))
a=0
score=0
while a<36:
    question_state=states_list[a]
    answer_input = int(screen.textinput(title="guess the  states and UTs",
                                     prompt=f"where's  the {question_state}"))
    answer_no=data[data["state"] == question_state].no.item()
    if answer_input==answer_no:
        score+=1
        guessed_states.append(question_state)
#         state=data[data["state"]==answer_input]
        messagebox.showinfo(title=f"answer is {answer_no}", message=f"you guessed it correct ,your score is {score}/36")
    elif answer_input == 0:
        break
    else:
        messagebox.showinfo(title=f"answer is {answer_no}", message=f"wrong answer your score is {score}/36")
    a += 1
missed_states = [state for state in states_list if state not in guessed_states]
for state in missed_states:
    new_state = data[data["state"] == state]
    t = turtle.Turtle()
    t.color("red")
    t.penup()
    t.goto(int(new_state.x), int(new_state.y))
    t.hideturtle()
    t.write(state, font=("ariel", 10, "bold"))

pandas.DataFrame(missed_states).to_csv("missed_states.csv")
messagebox.showinfo(title="quiz completed", message=f"your score is {score}/36")

screen.exitonclick()