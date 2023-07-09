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
                              prompt="What's another state name")
    # ans_state = ans_state.title()
    if ans_state is not None:
        ans_state = ans_state.title()
    elif ans_state == "Exit" or ans_state == "" or ans_state is None:
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
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())

if len(missing_states) == 0:
    pass
else:
    missed = {
        "Missed states": missing_states
    }
    final = pandas.DataFrame(missed)
    final.to_csv("Missed state names.csv")
