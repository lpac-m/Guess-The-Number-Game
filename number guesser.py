import random
from tkinter import *

#random number generator function
def take_number():
    number.set(random.randint(0,100))
    number_lbl.configure(text='Number Taken')

    result_lbl.pack_forget()
    result_lbl2.pack_forget()
    guess_count.set(0)
    #print(number.get())

#Guess evaluation function
def make_guess():
    guess_count.set(guess_count.get()+1)
    if guess.get()<number.get():
        result_lbl.configure(text='You guessed too LOW')
        result_lbl.pack()

    elif guess.get()>number.get():
        result_lbl.configure(text='You guessed too HIGHT')
        result_lbl.pack()

    elif guess.get()==number.get():
        result_lbl.configure(text='CONGRATULATIONS!You guessed RIGHT')
        result_lbl.pack()
        result_lbl2.pack()

    #print(str(number.get())+','+str(guess.get()))

#main window setup
main_window = Tk()
main_window.title('Number Guesser v1')
main_window.geometry('400x200')

number_frame = Frame(main_window)
guess_frame = Frame(main_window)
dev_frame = Frame(main_window)
number_frame.grid(row=0)
guess_frame.grid(row=1)
dev_frame.grid(row=2)

#variables
number=IntVar()
guess = IntVar()
guess_count = IntVar()

#Number GUI
number_lbl = Label(number_frame,text="No number taken")
number_lbl.pack()
number_btn = Button(number_frame,text='Take a number',command=lambda:take_number())
number_btn.pack()

#Guess GUI
guess_lbl = Label(guess_frame,text='Make your guess between 0-100:')
guess_lbl.pack()
guess_entry = Entry(guess_frame,textvariable=guess)
guess_entry.pack()
guess_btn = Button(guess_frame,text="Guess",command=lambda:make_guess())
guess_btn.pack()
counter_lbl = Label(guess_frame,textvariable=guess_count)
counter_lbl.pack()

#result display
result_lbl = Label(guess_frame)
result_lbl2 = Label(guess_frame,text="Take another number")

dev_lbl = Label(dev_frame,text='made by lpac-m',justify='left',padx=150,pady=50)
dev_lbl.pack()

main_window.mainloop()


    


