from tkinter import *

# Questions, Options, and Answers
questions = [
    "1. What is the capital of India?",
    "2. Who developed Python?",
    "3. What does CPU stand for?",
    "4. Which company developed Java?",
    "5. What is the value of 5 + 7?"
]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"],
    ["Central Processing Unit", "Central Power Unit", "Control Panel Unit", "Central Program Unit"],
    ["Sun Microsystems", "Google", "Microsoft", "IBM"],
    ["10", "11", "12", "13"]
]

answers = [0, 0, 0, 0, 2]

index = 0
score = 0

def next_question():
    global index, score
    if var.get() == answers[index]:
        score += 1
    index += 1

    if index == len(questions):
        display_result()
    else:
        display_question()

def display_question():
    global index
    question_label.config(text=questions[index])
    for i in range(4):
        radio_btns[i].config(text=options[index][i])
    var.set(-1)

def display_result():
    question_label.config(text=f"Your Score: {score}/{len(questions)}")
    for btn in radio_btns:
        btn.pack_forget()
    next_btn.pack_forget()

root = Tk()
root.title("Online Quiz Application")
root.geometry("500x350")

question_label = Label(root, text="", font=("Arial", 14), wraplength=400, justify="left")
question_label.pack(pady=20)

var = IntVar()
radio_btns = []
for i in range(4):
    rb = Radiobutton(root, text="", variable=var, value=i, font=("Arial", 12))
    rb.pack(anchor="w")
    radio_btns.append(rb)

next_btn = Button(root, text="Next", command=next_question, font=("Arial", 12), bg="skyblue")
next_btn.pack(pady=20)

display_question()
root.mainloop()
