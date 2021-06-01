import turtle
import pandas

# setup the screen and turtle
screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.penup()

guessed_states = []
# read data using pandas
data = pandas.read_csv("50_states.csv")
states = data["state"]
# check if user haven't yet guessed all of the states
while len(guessed_states) < 50:

    answer = screen.textinput(f"{len(guessed_states)}/50 states correct.", "What's another state name?").title()
    if answer in data["state"].values:
        guessed_states.append(answer)
        index = data[data["state"] == answer].index.values[0]
        x_coord = data.loc[index, "x"]
        y_coord = data.loc[index, "y"]
        my_turtle.goto(x_coord, y_coord)
        my_turtle.write(answer)
    else:
        continue

turtle.mainloop()
