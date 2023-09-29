from tkinter import *
import pandas, pyperclip
from random import choice, randint, shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


def save_details():
    details = {'website': website_input.get(), 'email': email_input.get(), 'pass': pass_input.get()}
    df = pandas.DataFrame(details, index=[0])
    with open('data.csv', 'a') as file:
        (df.to_csv(file, sep='|', index=False, header=file.tell() == 0))
    website_input.delete(0, END)
    pass_input.delete(0, END)

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

bg_image = PhotoImage(file='./logo.png')
canvas.create_image(150, 80, image=bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website')
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text='Label')
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0,'@gmail.com')
email_input.grid(row=2, column=1, columnspan=2)


pass_label = Label(text='Password')
pass_label.grid(row=3, column=0)
pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)


generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_details)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()