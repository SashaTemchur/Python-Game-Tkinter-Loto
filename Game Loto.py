from tkinter import *
import random as ran
from random import *
from tkinter import messagebox


root = Tk()
root.title("Loto")


p1 = randint(0, 90)
p2 = randint(0, 90)
p3 = randint(0, 90)
p4 = randint(0, 90)
p5 = randint(0, 90)
p6 = randint(0, 90)
p7 = randint(0, 90)
p8 = randint(0, 90)
p9 = randint(0, 90)
p10 = randint(0, 90)
p11 = randint(0, 90)
p12 = randint(0, 90)
p13 = randint(0, 90)
p14 = randint(0, 90)
p15 = randint(0, 90)

c1 = randint(0, 90)
c2 = randint(0, 90)
c3 = randint(0, 90)
c4 = randint(0, 90)
c5 = randint(0, 90)
c6 = randint(0, 90)
c7 = randint(0, 90)
c8 = randint(0, 90)
c9 = randint(0, 90)
c10 = randint(0, 5)
c11 = randint(0, 90)
c12 = randint(0, 90)
c13 = randint(0, 90)
c14 = randint(0, 90)
c15 = randint(0, 90)

b = randint(0, 90)

c_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]
p_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]


player_frm = Frame(root, width=150, height=150)
computer_frm = Frame(root, width=150, height=150)
bag_frm = Frame(root, width=150, height=150)

player_frm.pack(side=LEFT, fill=BOTH, expand=True)
computer_frm.pack(side=RIGHT, fill=BOTH, expand=True)
bag_frm.pack(fill=BOTH, expand=True)

card_player_txt = Text(player_frm, width=23, height=5)
card_player_txt.grid(padx=5, pady=15, row=5, column=0)

card_player_txt.insert('1.0', "-------Your-Card-------\n \
{}   {}   {}  {}   {} \n {}  {}   {}  {}   {} \n {}  {}    {}    {}  {}\n\
--------Your-Card------".format(p_list[0], p_list[1], p_list[2], p_list[3], p_list[4], p_list[5], p_list[6], p_list[7], p_list[8], p_list[9], p_list[10], p_list[11], p_list[12], p_list[13], p_list[14]))
card_computer_txt = Text(computer_frm, width=23, height=5)
card_computer_txt.grid(padx=5, pady=15, row=5, column=0)

card_computer_txt.insert('1.0', "-----Computer-Card-----\n \
{}   {}   {}  {}   {} \n {}  {}   {}  {}   {} \n {}  {}    {}    {}  {}\n\
-----Computer-Card-----".format(c_list[0], c_list[1], c_list[2], c_list[3], c_list[4], c_list[5], c_list[6], c_list[7], c_list[8], c_list[9], c_list[10], c_list[11], c_list[12], c_list[13], c_list[14]))


def delete_loto():
    global b
    global card_player_txt
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    global p13
    global p14
    global p15
    if p1 == b:
        p1 = '-'
        card_player_txt.delete('2.1', '2.3')
        card_player_txt.insert('2.1', ' ')
        card_player_txt.insert('2.2', '-')

    elif p2 == b:
        p2 = '-'
        card_player_txt.delete('2.6', '2.8')
        card_player_txt.insert('2.6', ' ')
        card_player_txt.insert('2.7', '-')

    elif p3 == b:
        p3 = '-'
        card_player_txt.delete('2.11', '2.13')
        card_player_txt.insert('2.11', ' ')
        card_player_txt.insert('2.12', '-')

    elif p4 == b:
        p4 = '-'
        card_player_txt.delete('2.15', '2.17')
        card_player_txt.insert('2.15', ' ')
        card_player_txt.insert('2.16', '-')

    elif p5 == b:
        p5 = '-'
        card_player_txt.delete('2.20', '2.22')
        card_player_txt.insert('2.20', ' ')
        card_player_txt.insert('2.21', '-')

    elif p6 == b:
        p6 = '-'
        card_player_txt.delete('3.1', '3.3')
        card_player_txt.insert('3.1', ' ')
        card_player_txt.insert('3.2', '-')

    elif p7 == b:
        p7 = '-'
        card_player_txt.delete('3.5', '3.7')
        card_player_txt.insert('3.5', ' ')
        card_player_txt.insert('3.6', '-')

    elif p8 == b:
        p8 = '-'
        card_player_txt.delete('3.10', '3.12')
        card_player_txt.insert('3.10', ' ')
        card_player_txt.insert('3.11', '-')

    elif p9 == b:
        p9 = '-'
        card_player_txt.delete('3.14', '3.16')
        card_player_txt.insert('3.14', ' ')
        card_player_txt.insert('3.15', '-')

    elif p10 == b:
        p10 = '-'
        card_player_txt.delete('3.19', '3.22')
        card_player_txt.insert('3.19', ' ')
        card_player_txt.insert('3.20', ' ')
        card_player_txt.insert('3.21', '-')

    elif p11 == b:
        p11 = '-'
        card_player_txt.delete('4.1', '4.3')
        card_player_txt.insert('4.1', ' ')
        card_player_txt.insert('4.2', '-')

    elif p12 == b:
        p12 = '-'
        card_player_txt.delete('4.5', '4.7')
        card_player_txt.insert('4.5', ' ')
        card_player_txt.insert('4.6', '-')

    elif p13 == b:
        p13 = '-'
        card_player_txt.delete('4.11', '4.13')
        card_player_txt.insert('4.11', ' ')
        card_player_txt.insert('4.12', '-')

    elif p14 == b:
        p14 = '-'
        card_player_txt.delete('4.17', '4.19')
        card_player_txt.insert('4.17', ' ')
        card_player_txt.insert('4.18', '-')

    elif p15 == b:
        p15 = '-'
        card_player_txt.delete('4.21', '4.23')
        card_player_txt.insert('4.21', ' ')
        card_player_txt.insert('4.22', '-')

    else:
        messagebox.showinfo('Information', 'You lost')
        root.destroy()
        lost = Tk()
        lost.title("Game over")
        l = Label(lost, width=30, text="GAME OVER")
        l.pack()
        lost.mainloop()
    if p1 == '-' and p2 == '-' and p3 == '-' and p4 == '-' and p5 == '-' and p6 == '-' and p7 == '-' and p8 == '-' and p9 == '-' and p10 == '-' and p11 == '-' and p12 == '-' and p13 == '-' and p14 == '-' and p15 == '-':
        messagebox.showinfo('WIN!', 'You WIN!')
        root.destroy()
        win_player = Tk()
        win_lbl = Label(win_player, width=30, text="YOU WIN!!!!")
        win_lbl.pack()
        win_player.mainloop()


def continue_loto():
    global b
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global card_computer_txt
    if p1 == b or p2 == b or p3 == b or p4 == b or p5 == b or p6 == b or p7 == b or p8 == b or p9 == b or p10 == b or p11 == b or p12 == b or p13 == b or p14 == b or p15 == b:
        messagebox.showinfo('Information', 'You lost')
        root.destroy()
        lost = Tk()
        lost.title("Game over")
        l = Label(lost, width=30, text="GAME OVER")
        l.pack()
        lost.mainloop()
    elif c1 == b:
        c1 = '-'
        card_computer_txt.delete('2.1', '2.3')
        card_computer_txt.insert('2.1', ' ')
        card_computer_txt.insert('2.2', '-')

    elif c2 == b:
        c2 = '-'
        card_computer_txt.delete('2.6', '2.8')
        card_computer_txt.insert('2.6', ' ')
        card_computer_txt.insert('2.7', '-')

    elif c3 == b:
        c3 = '-'
        card_computer_txt.delete('2.11', '2.13')
        card_computer_txt.insert('2.11', ' ')
        card_computer_txt.insert('2.12', '-')

    elif c4 == b:
        c4 = '-'
        card_computer_txt.delete('2.15', '2.17')
        card_computer_txt.insert('2.15', ' ')
        card_computer_txt.insert('2.16', '-')

    elif c5 == b:
        c5 = '-'
        card_computer_txt.delete('2.20', '2.22')
        card_computer_txt.insert('2.20', ' ')
        card_computer_txt.insert('2.21', '-')

    elif c6 == b:
        c6 = '-'
        card_computer_txt.delete('3.1', '3.3')
        card_computer_txt.insert('3.1', ' ')
        card_computer_txt.insert('3.2', '-')

    elif c7 == b:
        c7 = '-'
        card_computer_txt.delete('3.5', '3.7')
        card_computer_txt.insert('3.5', ' ')
        card_computer_txt.insert('3.6', '-')

    elif c8 == b:
        c8 = '-'
        card_computer_txt.delete('3.10', '3.12')
        card_computer_txt.insert('3.10', ' ')
        card_computer_txt.insert('3.11', '-')

    elif c9 == b:
        c9 = '-'
        card_computer_txt.delete('3.14', '3.16')
        card_computer_txt.insert('3.14', ' ')
        card_computer_txt.insert('3.15', '-')

    elif c10 == b:
        c10 = '-'
        card_computer_txt.delete('3.19', '3.21')
        card_computer_txt.insert('3.19', ' ')
        card_computer_txt.insert('3.20', '-')

    elif c11 == b:
        c11 = '-'
        card_computer_txt.delete('4.1', '4.3')
        card_computer_txt.insert('4.1', ' ')
        card_computer_txt.insert('4.2', '-')

    elif c12 == b:
        c12 = '-'
        card_computer_txt.delete('4.5', '4.7')
        card_computer_txt.insert('4.5', ' ')
        card_computer_txt.insert('4.6', '-')

    elif c13 == b:
        c13 = '-'
        card_computer_txt.delete('4.11', '4.13')
        card_computer_txt.insert('4.11', ' ')
        card_computer_txt.insert('4.12', '-')
    elif c14 == b:
        c14 = '-'
        card_computer_txt.delete('4.17', '4.19')
        card_computer_txt.insert('4.17', ' ')
        card_computer_txt.insert('4.18', '-')

    elif c15 == b:
        c15 = '-'
        card_computer_txt.delete('4.21', '4.23')
        card_computer_txt.insert('4.21', ' ')
        card_computer_txt.insert('4.22', '-')

    else:
        for b in range(randint(0, 90)):
            bag_lbl = Label(bag_frm, width=30, text="{}".format(b))
            bag_lbl.grid(padx=5, pady=5, row=2, column=0)

    if c1 == '-' and c2 == '-' and c3 == '-' and c4 == '-' and c5 == '-' and c6 == '-' and c7 == '-' and c8 == '-' and c9 == '-' and c10 == '-' and c11 == '-' and c12 == '-' and c13 == '-' and c14 == '-' and c15 == '-':
        messagebox.showinfo('WIN!', 'Computer WIN!')
        root.destroy()
        win_player = Tk()
        win_lbl = Label(win_player, width=30, text="COMPUTER WIN!!!!")
        win_lbl.pack()
        win_player.mainloop()


def bag_menu():
    global b
    bag_lbl = Label(bag_frm, width=30, text="{}".format(b))
    bag_lbl.grid(padx=5, pady=5, row=2, column=0)

    bag_lbl_lbl = Label(bag_frm, width=30, text="New barrel:")
    bag_lbl_lbl.grid(padx=5, pady=5, row=1, column=0)
    delete_btn = Button(bag_frm, width=30,
                        text="Cross out the number", command=delete_loto)
    delete_btn.grid(padx=5, pady=5, row=3, column=0)

    continue_btn = Button(
        bag_frm, width=30, text="Continue", command=continue_loto)
    continue_btn.grid(padx=5, pady=5, row=4, column=0)


player_lbl = Label(player_frm, width=30, text="Player menu")
player_lbl.grid(padx=5, pady=5, row=0, column=0)


Bag_btn = Button(bag_frm, width=30,
                 text="Throw the mouse", command=bag_menu)
Bag_btn.grid(padx=5, pady=5, row=3, column=0)

computer_lbl = Label(computer_frm, width=30, text="Computer menu")
computer_lbl.grid(padx=5, pady=5, row=0, column=0)


root.mainloop()
