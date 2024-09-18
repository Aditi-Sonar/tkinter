import tkinter
import random

m = tkinter.Tk()
m.title("Dice roll simulator")
m.minsize(800, 400)
m.maxsize(1000, 500)
m.configure(bg='#96DED1')

# Create a label to display "DICE ROLL SIMULATOR"
l = tkinter.Label(m, text='DICE ROLL SIMULATOR', font=('Courier', 12))
l.pack()

# Create a label to display the dice patterns
label = tkinter.Label(m, text="", font=("Courier", 180), bg='#96DED1')
label.pack()


# Function to roll the dice 
def dice_roll():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result = random.choice(value)
    label.configure(text=result)
    if result == '\u2680':
        label3 = tkinter.Label(m, text='You rolled a one! Click roll dice to roll again.', font=('arial', 10))
    elif result == '\u2681':
        label3 = tkinter.Label(m, text='You rolled a two! Click roll dice to roll again.', font=('arial', 10))
    elif result == '\u2682':
        label3 = tkinter.Label(m, text='You rolled a three! Click roll dice to roll again.', font=('arial', 10))
    elif result == '\u2683':
        label3 = tkinter.Label(m, text='You rolled a four! Click roll dice to roll again.', font=('arial', 10))
    elif result == '\u2684':
        label3 = tkinter.Label(m, text='You rolled a five! Click roll dice to roll again.', font=('arial', 10))
    elif result == '\u2685':
        label3 = tkinter.Label(m, text='You rolled a six! Click roll dice to roll again.', font=('arial', 10))
    label3.place(relx=0.5, rely=0.8, anchor='center')
# Button to roll the dice
button = tkinter.Button(m, text="ROLL", command=dice_roll, fg='white', bg='black', width=10, font=('Helvetica', 12))
button.place(relx=0.5, rely=0.6, anchor='center')

m.mainloop()
