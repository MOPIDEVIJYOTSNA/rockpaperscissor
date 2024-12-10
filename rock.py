from tkinter import *
import random
# Initialize Tkinter window
rps = Tk()  # Corrected `TK()` to `Tk()`
rps.geometry("300x300")  # Fixed typo `geomentry` to `geometry`
rps.title("Rock Paper Scissors")

# Initialize scores
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""


# Helper functions
def choice_to_number(choice):
    rps_dict = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps_dict[choice]


def number_to_choice(number):
    rps_dict = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps_dict[number]


def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])


def result(human_choice, comp_choice):
    global user_score
    global comp_score

    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    # Determine result
    if user == comp:
        outcome = "It's a Tie!"
    elif (user - comp) % 3 == 1:
        outcome = "You Win!"
        user_score += 1
    else:
        outcome = "Computer Wins!"
        comp_score += 1

    # Display result
    text_area = Text(master=rps, font=("arial", 12, "bold"), relief=RIDGE, bg="#033642", fg="white", height=6, width=35)
    text_area.grid(column=0, row=4)
    result_text = (
        f"Your Choice: {human_choice}\n"
        f"Computer's Choice: {comp_choice}\n"
        f"Result: {outcome}\n"
        f"Your Score: {user_score}\n"
        f"Computer Score: {comp_score}"
    )
    text_area.insert(END, result_text)


# Button functions
def rock():
    global user_choice, comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def paper():
    global user_choice, comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def scissor():
    global user_choice, comp_choice
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


# Create Buttons
button_rock = Button(
    text="ROCK", bg="#308487", font=("arial", 15, "bold"), relief=RIDGE,
    activebackground="#059458", activeforeground="white", width=24, command=rock
)
button_rock.grid(column=0, row=1)

button_paper = Button(
    text="PAPER", bg="#308487", font=("arial", 15, "bold"), relief=RIDGE,
    activebackground="#F2EECB", activeforeground="white", width=24, command=paper
)
button_paper.grid(column=0, row=2)

button_scissor = Button(
    text="SCISSOR", bg="#308487", font=("arial", 15, "bold"), relief=RIDGE,
    activebackground="#067022", activeforeground="white", width=24, command=scissor
)
button_scissor.grid(column=0, row=3)

# Run the Tkinter loop
rps.mainloop()
