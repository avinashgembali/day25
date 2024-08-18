import turtle
from turtle import Screen, Turtle
import pandas

s = Screen()
s.title("U.S.STATES GAME")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct = 0
total = 50
is_completed = False
guessed_states = []
while not is_completed:
    answer = s.textinput(title=f"{correct}/{total} states correct", prompt="What's another state name ?").title()
    if answer == "Exit":
        # learn.csv
        # we can also simply add to missing list and create a csv otherwise using dictionary also not a problem
        learn_dict = {
            "states": [],
            "x": [],
            "y": []
        }
        list_states = data["state"].to_list()
        for state in list_states:
            if state in guessed_states:
                continue
            else:
                row = data[data["state"] == state]
                learn_dict["states"].append(row["state"].item())
                learn_dict["x"].append(row["x"].item())
                learn_dict["y"].append(row["y"].item())
        learn_state_data = pandas.DataFrame(learn_dict)
        learn_state_data.to_csv("learn_states.csv")
        break
    if answer in data["state"].values:
        guessed_states.append(answer)
        row = data[data["state"] == answer]
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(row["x"].item()), int(row["y"].item()))
        t.write(arg=row["state"].item(), move=False, align="center", font=("Arial", 5, "bold"))
        correct += 1
    if correct == total:
        is_completed = True

