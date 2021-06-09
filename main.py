from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    global pass_entry

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(numbers) for _ in range(randint(2, 4))] + \
                    [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pass_entry.clipboard_clear()
    pass_entry.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    global web_entry
    global email_entry
    global pass_entry

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid entry", message="Must fill in all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password}\nIs it ok to save?")

        # format:
        # Website | Email/Username | password
        # save it to data.txt

        if is_ok:
            with open("data.txt", "a") as my_file:
                my_file.write(f"{website} | {email} | {password}\n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=60)
window.title("Password Manager")

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0, sticky=E)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, sticky=E)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0, sticky=E)

web_entry = Entry(width=55)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
web_entry.focus_set()

email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)

pass_entry = Entry(width=30)
pass_entry.grid(row=3, column=1, sticky=W)

gen_pass_button = Button(text="Generate Password", width=18, command=generate_password)
gen_pass_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="Add", width=47, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

email_entry.insert(0, "example@example.com")

window.mainloop()