import random
from tkinter import *

#random number generator function
def take_number():
    number = random.randint(0,9)
    number_lbl.configure(text='Number Taken')
    print(number)

def make_guess():
    if guess.get()<number.get():
        result_lbl.configure(text='You guessed too LOW')

    elif guess.get()>number.get():
        result_lbl.configure(text='You guessed too HIGHT')

    elif guess.get()==number.get():
        result_lbl.configure(text='CONGRATULATIONS!You guessed RIGHT')


#main window setup
main_window = Tk()
main_window.title('Number Guesser')
main_window.geometry('400x400')

number_frame = Frame(main_window).pack()
guess_frame = Frame(main_window).pack()

#variables
number=IntVar()
guess = IntVar()

#Number GUI
number_lbl = Label(number_frame,text="No number taken")
number_lbl.pack()
number_btn = Button(number_frame,text='Take a number',command=lambda:take_number())
number_btn.pack()

#Guess GUI
guess_lbl = Label(guess_frame,text='Make your guess:')
guess_lbl.pack()
guess_entry = Entry(guess_frame,textvariable=guess)
guess_entry.pack()
guess_btn = Button(guess_frame,text="Guess",command=lambda:make_guess())
guess_btn.pack()

#result display
result_lbl = Label(guess_frame)
result_lbl.pack()

main_window.mainloop()


    


