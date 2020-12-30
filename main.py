from tkinter import *
from tkinter import messagebox
import json
import password_generator as pass_gen
import pyperclip

# ---------------------- Constants ------------------ #
DEFAULT_EMAIL = "gnanaganesh1999@gmail.com"


# ---------------------- Password generator ---------- #
def display_password():
    password_entry.delete(0, END)
    new_password = pass_gen.generate_password()
    pyperclip.copy(new_password)
    password_entry.insert(0, new_password)


# --------------------- Search Password ------------- #
def search_website():
    website = website_entry.get()
    if website == "":
        messagebox.showwarning(title="Website Not Found", message="Please Enter Website Name to search for Password.")
    else:
        try:
            data_file = open("data.json")
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
        except (FileNotFoundError, KeyError):
            messagebox.showwarning(title="Website Not Found", message="Please Save your Credentials before Searching.")
        else:
            pyperclip.copy(password)
            messagebox.showinfo(title=website + " Credentials",
                                message=f"\nEmail : {email}\nPassword : {password}\n\n"
                                        f"Note: Your password is copied to Clipboard.")
            reset_entries()


# ---------------------- Save Password ---------------#
def save_details_to_file():
    website_name = website_entry.get()
    email_or_username = email_entry.get()
    password = password_entry.get()
    new_data = {website_name: {
        "email": email_or_username,
        "password": password
    }}
    if website_name != "" and email_or_username != "" and password != "":
        is_overwrite = True
        try:
            data_file = open("data.json")
        except FileNotFoundError:
            data = new_data
        else:
            data = json.load(data_file)
            try:
                prev_data = data[website_name]
            except KeyError:
                prev_data = ''

            if prev_data != "":
                is_overwrite = messagebox.askyesno(title=website_name + " Already Exists",
                                                   message=f"Overwrite the previous password ?\n\nEmail : "
                                                           f"{prev_data['email']}\nPassword : {prev_data['password']}")
            data.update(new_data)
            print(data)
        finally:
            if is_overwrite:
                data_file = open("data.json", mode="w")
                json.dump(data, data_file, indent=4)
                data_file.close()
                messagebox.showinfo(title=website_name + " Credentials", message="Saved Successfully !")
                reset_entries()
    else:
        messagebox.showwarning(title="OOPS", message="Please Enter all the fields before saving !")


# ---------------------- UI Setup ------------------- #
def reset_entries():
    website_entry.delete(0, END)
    website_entry.focus()
    email_entry.delete(0, END)
    email_entry.insert(0, DEFAULT_EMAIL)
    password_entry.delete(0, END)


# Window
root = Tk()
root.title("G&G Password Manager")
root.resizable(False, False)
root.config(padx=20, pady=20, bg="#fff5f5")

# Canvas
canvas = Canvas(width=150, height=200, highlightthickness=0, bg="#fff5f5")
logo_img = PhotoImage(file="G&G.png")
canvas.create_image(75, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website :", bg="#fff5f5", fg="#0d3858", highlightthickness=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/ Username : ", bg="#fff5f5", fg="#0d3858", highlightthickness=0)
email_label.grid(column=0, row=2)

password_label = Label(text="Password : ", bg="#fff5f5", fg="#0d3858", highlightthickness=0)
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=23, highlightthickness=0, bg="#f0f0f0")
website_entry.grid(column=1, row=1, padx=3, pady=3)

email_entry = Entry(width=42, highlightthickness=0, bg="#f0f0f0")
email_entry.grid(column=1, row=2, columnspan=2, padx=3, pady=3)

password_entry = Entry(width=23, highlightthickness=0, bg="#f0f0f0")
password_entry.grid(column=1, row=3, padx=3, pady=3)

# Buttons
generate_button = Button(text="Generate Password", command=display_password, bg="#fff", fg="#000",
                         highlightthickness=0)
generate_button.grid(column=2, row=3, padx=3, pady=3)

search_button = Button(text="Search", command=search_website, width=14, bg="#a2861d", fg="white", highlightthickness=0)
search_button.grid(column=2, row=1, padx=3, pady=3)

add_button = Button(text="Add", command=save_details_to_file, width=36, bg="#f4bc33", fg="#fff5f5",
                    highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, padx=3, pady=3)

# Function Calls
root.eval('tk::PlaceWindow . center')
reset_entries()
root.mainloop()
