import turtle
import pandas

mys = turtle.Screen()
mys.title("State guessing name")
image = "state.gif"
mys.addshape(image)
turtle.shape(image)

# ---Gives coordinates of clicked location---
# def get_mouse_click_coor(x, y):
#     print(x, y)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    ans_state = mys.textinput(title=f"{len(guessed_states)}/50 states guessed",
                              prompt="What's another state name").title()
    if ans_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        break
    if ans_state in all_states:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

if len(missing_states) == 0:
    pass
else:
    missed = {
        "Missed states": missing_states
    }
    final = pandas.DataFrame(missed)
    final.to_csv("Missed state names.csv")
