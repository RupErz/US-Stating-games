import turtle
import pandas
FONT = ('Arial', 8, 'normal')
ALIGN = "center"
screen = turtle.Screen()
screen.title("Nghia-US Stating Games")
new_shape = "blank_states_img.gif"
screen.addshape(new_shape)
#add another shape options for turtle
background_turtle = turtle.Turtle(new_shape)

data = pandas.read_csv("50_states.csv")
state = data["state"]
state_list = state.to_list()
def draw_state(state_name):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    row = data[data.state == state_name ] #get the row we need to extract data
    #it because the data.state is title case not lower case so we cant compare it!
    # index = row.index[0]
    #take the index of the rows !!
    # x_cor = row.x
    # y_cor = row.y
    # new_turtle.goto(x_cor[index], y_cor[index])
    new_turtle.goto(int(row.x), int(row.y))
    new_turtle.write(state_name, False, ALIGN, FONT)

def check_overlap(list, answer):
    result = False
    for i in list :
        if i.lower() == answer.lower() :
            result = True
    return result

correct_answer = 0
answer = (screen.textinput("Guess the state", "What is the other state name?")).title()
prevent_old_answer = []
while correct_answer != 50 :
    if answer == "Exit":
        break
    # if check_result(answer) : #if return true
    if answer in state_list :
        if not check_overlap(prevent_old_answer, answer) :
            correct_answer += 1
            draw_state(answer)
            prevent_old_answer.append(answer)
    answer = screen.textinput(f"{correct_answer}/50 States Correct", "What is the other state name?").title()
#Create a csv file for state we dont know
state_not_know = [state for state in state_list if state not in prevent_old_answer]
new_data = {"State" : state_not_know}
file = pandas.DataFrame(new_data)
file.to_csv("ToLearn.csv")

