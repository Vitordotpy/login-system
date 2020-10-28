import tkinter
import sqlite3
from tkinter import *


conn = sqlite3.connect('users.db')
cur = conn.cursor()

def login():
    user_id = login_entry.get()
    user_p = password_entry.get()
    cur.execute('''SELECT user_id FROM user WHERE user_name=? ''', (user_id, ))
    id_tuple = cur.fetchone()
    id = id_tuple[0]
    cur.execute('''SELECT user_pass FROM user_pass WHERE pass_id=? ''', (id, ))
    auth_tuple = cur.fetchone()
    auth = auth_tuple[0]
    if str(user_p) == str(auth):
        exit()
        return True
    else:
        output.insert(END, 'incorrect user or pass\n')


def registring():
    def register_commit():
        registred_username = r_username_entry.get()
        registred_password = r_userpass_entry.get()
        pass_confirm = confirm_pass_entry.get()
        if registred_password != pass_confirm:
            error['text'] = 'password divergence'
            return
        cur.execute('''INSERT INTO user(user_name) VALUES(?)''', (registred_username,))
        cur.execute('''INSERT INTO user_pass(user_pass) VALUES(?)''', (registred_password,))
        error['text'] = 'registred'
        conn.commit()
        return

    while True:
        register_sc = tkinter.Tk()
        register_sc.title('register')

        register_text = tkinter.Label(register_sc, text='REGISTER')
        register_text.grid(column=1, row=0)

        # username text and inputbox

        r_username = tkinter.Label(register_sc, text='username ')
        r_username.grid(column=0, row=1)

        r_username_entry = tkinter.Entry(register_sc)
        r_username_entry.grid(column=1, row=1)

        # userpass and inputbox

        r_userpass = tkinter.Label(register_sc, text='password ')
        r_userpass.grid(column=0, row=2)

        r_userpass_entry = tkinter.Entry(register_sc)
        r_userpass_entry.grid(column=1, row=2)

        # confirma password text and inputbox

        confirm_pass = tkinter.Label(register_sc, text='confirm ')
        confirm_pass.grid(column=0, row=3)

        confirm_pass_entry = tkinter.Entry(register_sc)
        confirm_pass_entry.grid(column=1, row=3)

        # register button

        register_button = tkinter.Button(register_sc, text='register', command=register_commit)
        register_button.grid(column=0, row=4)

        error = tkinter.Label(register_sc, text='')
        error.grid(column=1, row=4)

        register_sc.mainloop()

while True:
    Login_sc = tkinter.Tk()
    Login_sc.title('login')

    login_text = tkinter.Label(Login_sc, text='LOGIN')
    login_text.grid(row=0)

    #user login

    user_login = tkinter.Label(Login_sc, text='User ')
    user_login.grid(column=0, row=1)

    login_entry = tkinter.Entry(Login_sc)
    login_entry.grid(column=1, row=1)

    #user password

    user_password = tkinter.Label(Login_sc, text='Password ')
    user_password.grid(column=0, row=2)

    password_entry = tkinter.Entry(Login_sc)
    password_entry.grid(column=1, row=2)

    #login button

    login_button = tkinter.Button(Login_sc, text='Login', command=login)
    login_button.grid(column=1, row=3)

    #register button

    register_button = tkinter.Button(Login_sc, text='register', command=registring)
    register_button.grid(column=0, row=3)

    output = Text(Login_sc, width=15, height=5, background='light grey')
    output.grid(column=1, row=4)

    Login_sc.mainloop()