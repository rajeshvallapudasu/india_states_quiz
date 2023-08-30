import turtle
import random
import pandas
screen=turtle.Screen()
screen.title("My Indian States game")
image="rajeshindia.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states_list=data["state"].to_list()
random.shuffle(states_list)
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
while a<36:
    question_state=states_list[a]
    answer_input = int(screen.textinput(title=f"{len(guessed_states)}/36 of total states and UTs",
                                     prompt=f"where's  the {question_state}"))
    if answer_input==data[data["state"] == question_state].no.item():
         guessed_states.append(question_state)
#         state=data[data["state"]==answer_input]

    elif answer_input==0:
        missed_states=[]
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        pandas.DataFrame(missed_states).to_csv("missed_states.csv")

        break
    a += 1

