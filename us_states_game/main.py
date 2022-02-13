import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


correct_answers=[]
data_state = pandas.read_csv("50_states.csv")
all_states = data_state.state.to_list()

while len(correct_answers)<50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 scores", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states = [i for i in all_states if i not in correct_answers]
        new_frame=pandas.DataFrame(missing_states)
        new_frame.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        state_data=data_state[data_state.state == answer_state]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(state_data.state.item())


