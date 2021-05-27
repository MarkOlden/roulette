
from math import radians
from os import read
from tkinter import *
import tkinter.font as tkFont
import random
from sys import exit, setprofile
import time



def bet():
    bet_window = Tk()
    def get_color(RadioValue):
        global color
        if RadioValue.get() == 0:
            color = 'red'
            bet_button.configure(text='RED')
            bet_window.destroy()
        elif RadioValue.get() == 1:
            color = 'black'
            bet_button.configure(text='BLACK')
            bet_window.destroy()
    bet_window.geometry('310x110+500+430')
    bet_window.title('New bet')
    main_label = Label(bet_window, text="Place your bets")
    RadioValue0 = IntVar(bet_window)
    RadioValue0.set(0)
    R_button0 = Radiobutton(bet_window, text='RED', variable=RadioValue0, value=0, padx=20)
    R_button1 = Radiobutton(bet_window, text='BLACK', variable=RadioValue0, value=1, padx=20)
    b = Button(bet_window, text='Bet', command=lambda:get_color(RadioValue0))
    main_label.pack()
    R_button0.pack(side=LEFT)
    R_button1.pack(side=RIGHT)
    b.pack(side=BOTTOM)
    bet_window.mainloop()


def spin():
    global k
    global color
    k += 1
    spin_button["state"] = "disabled"
    exit_button["state"] = "disabled"
    stats_button["state"] = "disabled"
    reset_button["state"] = "disabled"
    bet_button["state"] = "disabled"
    spin_button.configure(bg='white', fg='black')
    pause = 0.01
    for i in range(random.randint(10, 30)):
        sector = random.randint(0, 36)
        sector_label.configure(text=sector, bg=sectors[sector], fg='white')
        time.sleep(pause)
        pause += 0.02
        window.update()
    spin_button["state"] = "normal"
    exit_button["state"] = "normal"
    stats_button["state"] = "normal"
    reset_button["state"] = "normal"
    bet_button["state"] = "normal"
    bet_button.configure(text="BET")
    spin_button.configure(bg='green', fg='white')
    stats[sectors[sector]] += 1
    win_check(color, sector)
    del color


def win_check(color, sector):
    if color == sectors[sector]:
        print('WIN')
        bet_button.configure(text='WIN | BET')
    else:
        print('LOSE')
        bet_button.configure(text='LOSE | BET')


def show_stats():
    sector_label.configure(text='R: ' + str(stats['red']) + '\nB: ' + str(stats['black']) + '\nG: ' + str(stats['green']))
    sector_label.configure(bg='white', fg='black')


def reset_stats():
    global stats
    stats = {
    'red': 0,
    'black': 0,
    'green': 0
    }
    show_stats()


def popupScreen():
    popupRoot = Tk()
    # popupRoot.after(5000, exit)
    popupLabel = Label(popupRoot, text='Sure want to exit?', font = ("Verdana", 12))
    popupButton = Button(popupRoot, padx=100, text='Exit', command=exit, bg='black', fg='white')
    popupRoot.title('Bye')
    popupLabel.pack()
    popupButton.pack()
    popupRoot.geometry('200x50+700+500')
    popupRoot.mainloop()
    

def secret(event):
    global sec
    sec += 1
    if sec == 15:
        spin_button.configure(text='666')


sectors = {
    0: 'green',
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'black',
    12: 'red',
    13: 'black',
    14: 'red',
    15: 'black',
    16: 'red',
    17: 'black',
    18: 'red',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'black',
    30: 'red',
    31: 'black',
    32: 'red',
    33: 'black',
    34: 'red',
    35: 'black',
    36: 'red'
}
stats = {
    'red': 0,
    'black': 0,
    'green': 0
}
k = 0
sec = 0

window = Tk()
window.title('Roulette')
window.call('wm', 'iconphoto', window._w,PhotoImage(file='img/icon.png'))
window.resizable(width=False, height=False)
window.geometry('+500+200')
fontStyle = tkFont.Font(family="Lucida Grande", size=32)

sector_label = Label(window, text='Good luck!', font=fontStyle, width='12', height='4')
bet_button = Button(window, text='BET', command=bet, width='12', height='1', bg='yellow', fg='black', font=fontStyle)
spin_button = Button(window, text='SPIN', command=spin, width='12', height='1', bg = 'green', fg='white', font=fontStyle)
stats_button = Button(window, text='show stats', command=show_stats, width='14', height='1')
reset_button = Button(window, text='reset stats', command=reset_stats, width='13', height='1')
exit_button = Button(window, text='exit', command=popupScreen, width='13', height='1')
sector_label.pack()
bet_button.pack()
spin_button.pack()
stats_button.pack(side=LEFT)
reset_button.pack(side=LEFT)
exit_button.pack(side=LEFT)
stats_button.bind('<Button-1>', secret)

window.mainloop()
