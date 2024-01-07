from turtle import Turtle, Screen
import pandas

turtle = Turtle()
pen = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(height=600, width=800)
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's Name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        pandas.DataFrame(missed_states).to_csv("missed_states.csv")
        break
    if answer_state in states:
        coordinates = data[data.state == answer_state].to_dict()
        ind = states.index(answer_state)
        x_coor = coordinates["x"][ind]
        y_coor = coordinates["y"][ind]
        pen.hideturtle()
        pen.penup()
        pen.goto(x_coor, y_coor)
        pen.write(answer_state)
        guessed_states.append(answer_state)

# missed_states = []
# for state in states:
#     if state not in guessed_states:
#         missed_states.append(state)


