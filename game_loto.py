import random as ran # Imports a library random 
from random import * # Imports from library random all
from tkinter import * # Imports from library tkinter all
from tkinter import messagebox # Imports from library tkinter messagebox 
from loguru import logger

logger.add("loto_logs.log", format="{time} | {level} | {message}", rotation="100MB") # Додає файл куди зкладаються всі логи

root = Tk() # Make a window
root.title("Loto") # Gives the window a name


player_card_num1 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num2 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num3 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num4 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num5 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num6 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num7 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num8 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num9 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num10 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num11 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num12 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num13 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num14 = randint(0, 90) # Makes this change to a random number between 0 and 90
player_card_num15 = randint(0, 90) # Makes this change to a random number between 0 and 90

computer_card_num1 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num2 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num3 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num4 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num5 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num6 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num7 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num8 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num9 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num10 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num11 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num12 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num13 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num14 = randint(0, 90) # Makes this change to a random number between 0 and 90
computer_card_num15 = randint(0, 90) # Makes this change to a random number between 0 and 90

figure_with_bag = randint(0, 90) # Makes this change to a random number between 0 and 90

player_frm = Frame(root, width=150, height=150) # Makes a special window for the player
computer_frm = Frame(root, width=150, height=150) # Makes a special window for the computer
bag_frm = Frame(root, width=150, height=150) # Makes a special window for the pouch

player_frm.pack(side=LEFT, fill=BOTH, expand=True) # Close and display the window according to the parameters
computer_frm.pack(side=RIGHT, fill=BOTH, expand=True) # Close and display the window according to the parameters
bag_frm.pack(fill=BOTH, expand=True) # Close and display the window according to the parameters

card_player_txt = Text(player_frm, width=23, height=5) # Makes a card for the player
card_player_txt.grid(padx=5, pady=15, row=5, column=0) # Makes a card for the computer

card_computer_txt = Text(computer_frm, width=23, height=5) # Closes and places the player card in the desired place according to the parameters
card_computer_txt.grid(padx=5, pady=15, row=5, column=0) # Closes and places the computer card in the desired place according to the parameters


card_player_txt.insert('1.0', "-------Your-Card-------\n \
{}   {}   {}  {}   {} \n {}  {}   {}  {}   {} \n {}  {}    {}    {}  {}\n\
--------Your-Card------".format(player_card_num1, player_card_num2, player_card_num3, player_card_num4, player_card_num5, player_card_num6, player_card_num7, player_card_num8, player_card_num9, player_card_num10, player_card_num11, player_card_num12, player_card_num13, player_card_num14, player_card_num15)) # Makes a player card with numbers


card_computer_txt.insert('1.0', "-----Computer-Card-----\n \
{}   {}   {}  {}   {} \n {}  {}   {}  {}   {} \n {}  {}    {}    {}  {}\n\
-----Computer-Card-----".format(computer_card_num1, computer_card_num2, computer_card_num3, computer_card_num4, computer_card_num5, computer_card_num6, computer_card_num7, computer_card_num8, computer_card_num9, computer_card_num10, computer_card_num11, computer_card_num12, computer_card_num13, computer_card_num14, computer_card_num15)) # Makes a computer card with numbers


def delete_loto(): # Makes a function
    
    global figure_with_bag, card_player_txt, player_card_num1, player_card_num2, player_card_num3, player_card_num4, player_card_num5, player_card_num6, player_card_num7, player_card_num8, player_card_num9, player_card_num10, player_card_num11, player_card_num12, player_card_num13, player_card_num14, player_card_num15 # Declare these variables in a function
    if player_card_num1 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num1 = '-' # Changes the shift to "-"
        card_player_txt.delete('2.1', '2.3') # It deletes something at these coordinates
        card_player_txt.insert('2.1', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('2.2', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num2 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num2 = '-' # Changes the shift to "-"
        card_player_txt.delete('2.6', '2.8') # It deletes something at these coordinates
        card_player_txt.insert('2.6', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('2.7', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num3 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num3 = '-' # Changes the shift to "-"
        card_player_txt.delete('2.11', '2.13') # It deletes something at these coordinates
        card_player_txt.insert('2.11', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('2.12', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num4 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num4 = '-' # Changes the shift to "-"
        card_player_txt.delete('2.15', '2.17') # It deletes something at these coordinates
        card_player_txt.insert('2.15', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('2.16', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num5 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num5 = '-' # Changes the shift to "-"
        card_player_txt.delete('2.20', '2.22') # It deletes something at these coordinates
        card_player_txt.insert('2.20', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('2.21', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num6 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num6 = '-' # Changes the shift to "-"
        card_player_txt.delete('3.1', '3.3') # It deletes something at these coordinates
        card_player_txt.insert('3.1', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.2', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num7 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num7 = '-' # Changes the shift to "-"
        card_player_txt.delete('3.5', '3.7') # It deletes something at these coordinates
        card_player_txt.insert('3.5', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.6', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num8 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num8 = '-' # Changes the shift to "-"
        card_player_txt.delete('3.10', '3.12') # It deletes something at these coordinates
        card_player_txt.insert('3.10', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.11', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num9 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num9 = '-' #  Changes the shift to "-"
        card_player_txt.delete('3.14', '3.16') # It deletes something at these coordinates
        card_player_txt.insert('3.14', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.15', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num10 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num10 = '-' # Changes the shift to "-"
        card_player_txt.delete('3.19', '3.22') # It deletes something at these coordinates
        card_player_txt.insert('3.19', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.20', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('3.21', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num11 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num11 = '-' # Changes the shift to "-"
        card_player_txt.delete('4.1', '4.3') # It deletes something at these coordinates
        card_player_txt.insert('4.1', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('4.2', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num12 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num12 = '-' # Changes the shift to "-"
        card_player_txt.delete('4.5', '4.7') # It deletes something at these coordinates
        card_player_txt.insert('4.5', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('4.6', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num13 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num13 = '-' # Changes the shift to "-"
        card_player_txt.delete('4.11', '4.13') # It deletes something at these coordinates
        card_player_txt.insert('4.11', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('4.12', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num14 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num14 = '-' # Changes the shift to "-"
        card_player_txt.delete('4.17', '4.19') # It deletes something at these coordinates
        card_player_txt.insert('4.17', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('4.18', '-') # Inserts what we specified at the specified coordinates

    elif player_card_num15 == figure_with_bag: # If the number is equal to the number from the bag then
        player_card_num15 = '-' # Changes the shift to "-"
        card_player_txt.delete('4.21', '4.23') # It deletes something at these coordinates
        card_player_txt.insert('4.21', ' ') # Inserts what we specified at the specified coordinates
        card_player_txt.insert('4.22', '-') # Inserts what we specified at the specified coordinates

    else: # Otherwise
        messagebox.showinfo('Information', 'You lost') # Sends a message that you lost
        root.destroy() # Closes the main window
        lost = Tk() # Creates a new window
        lost.title("Game over") # Name this window as we specified
        l = Label(lost, width=30, text="GAME OVER") # It says that you lost
        l.pack() # Closes the label
        lost.mainloop() # Closes the program
    if player_card_num1 == '-' and player_card_num2 == '-' and player_card_num3 == '-' and player_card_num4 == '-' and player_card_num5 == '-' and player_card_num6 == '-' and player_card_num7 == '-' and player_card_num8 == '-' and player_card_num9 == '-' and player_card_num10 == '-' and player_card_num11 == '-' and player_card_num12 == '-' and player_card_num13 == '-' and player_card_num14 == '-' and player_card_num15 == '-': # If the variable is "-"
        messagebox.showinfo('WIN!', 'You WIN!') # Sends a message that you win
        root.destroy() # Closes the main window
        win_player = Tk() # Creates a new window
        win_player.title("You win") # Name this window as we specified
        win_lbl = Label(win_player, width=30, text="YOU WIN") # It says that you win
        win_lbl.pack() # Closes the label
        win_player.mainloop() # Closes the program
    
    
def continue_loto(): # Makes a function
    
    global figure_with_bag, computer_card_num1, computer_card_num2, computer_card_num3, computer_card_num4, computer_card_num5, computer_card_num6, computer_card_num7, computer_card_num8, computer_card_num9, computer_card_num10, computer_card_num11, computer_card_num12, computer_card_num13, computer_card_num14, computer_card_num15, card_computer_txt # Declare these variables in a function
    if player_card_num1 == figure_with_bag or player_card_num2 == figure_with_bag or player_card_num3 == figure_with_bag or player_card_num4 == figure_with_bag or player_card_num5 == figure_with_bag or player_card_num6 == figure_with_bag or player_card_num7 == figure_with_bag or player_card_num8 == figure_with_bag or player_card_num9 == figure_with_bag or player_card_num10 == figure_with_bag or player_card_num11 == figure_with_bag or player_card_num12 == figure_with_bag or player_card_num13 == figure_with_bag or player_card_num14 == figure_with_bag or player_card_num15 == figure_with_bag: # If the number is equal to the number from the bag then
        messagebox.showinfo('Information', 'You lost') # Sends a message that you lost
        root.destroy() # Closes the main window
        lost = Tk() # Creates a new window
        lost.title("Game over") # Name this window as we specified
        l = Label(lost, width=30, text="GAME OVER") # It says that you lost
        l.pack() # Closes the label
        lost.mainloop() # Closes the program
    elif computer_card_num1 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num1 = '-' # Changes the shift to "-"
        card_computer_txt.delete('2.1', '2.3') # It deletes something at these coordinates
        card_computer_txt.insert('2.1', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('2.2', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num2 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num2 = '-' # Changes the shift to "-"
        card_computer_txt.delete('2.6', '2.8') # It deletes something at these coordinates
        card_computer_txt.insert('2.6', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('2.7', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num3 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num3 = '-' # Changes the shift to "-"
        card_computer_txt.delete('2.11', '2.13') # It deletes something at these coordinates
        card_computer_txt.insert('2.11', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('2.12', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num4 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num4 = '-' # Changes the shift to "-"
        card_computer_txt.delete('2.15', '2.17') # It deletes something at these coordinates
        card_computer_txt.insert('2.15', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('2.16', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num5 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num5 = '-' # Changes the shift to "-"
        card_computer_txt.delete('2.20', '2.22') # It deletes something at these coordinates
        card_computer_txt.insert('2.20', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('2.21', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num6 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num6 = '-' # Changes the shift to "-"
        card_computer_txt.delete('3.1', '3.3') # It deletes something at these coordinates
        card_computer_txt.insert('3.1', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('3.2', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num7 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num7 = '-' # Changes the shift to "-"
        card_computer_txt.delete('3.5', '3.7') # It deletes something at these coordinates
        card_computer_txt.insert('3.5', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('3.6', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num8 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num8 = '-' # Changes the shift to "-"
        card_computer_txt.delete('3.10', '3.12') # It deletes something at these coordinates
        card_computer_txt.insert('3.10', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('3.11', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num9 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num9 = '-' # Changes the shift to "-"
        card_computer_txt.delete('3.14', '3.16') # It deletes something at these coordinates
        card_computer_txt.insert('3.14', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('3.15', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num10 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num10 = '-' # Changes the shift to "-"
        card_computer_txt.delete('3.19', '3.21') # It deletes something at these coordinates
        card_computer_txt.insert('3.19', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('3.20', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num11 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num11 = '-' # Changes the shift to "-"
        card_computer_txt.delete('4.1', '4.3') # It deletes something at these coordinates
        card_computer_txt.insert('4.1', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('4.2', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num12 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num12 = '-' # Changes the shift to "-"
        card_computer_txt.delete('4.5', '4.7') # It deletes something at these coordinates
        card_computer_txt.insert('4.5', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('4.6', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num13 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num13 = '-' # Changes the shift to "-"
        card_computer_txt.delete('4.11', '4.13') # It deletes something at these coordinates
        card_computer_txt.insert('4.11', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('4.12', '-') # Inserts what we specified at the specified coordinates
    elif computer_card_num14 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num14 = '-' # Changes the shift to "-"
        card_computer_txt.delete('4.17', '4.19') # It deletes something at these coordinates
        card_computer_txt.insert('4.17', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('4.18', '-') # Inserts what we specified at the specified coordinates

    elif computer_card_num15 == figure_with_bag: # If the number is equal to the number from the bag then
        computer_card_num15 = '-' # Changes the shift to "-"
        card_computer_txt.delete('4.21', '4.23') # It deletes something at these coordinates
        card_computer_txt.insert('4.21', ' ') # Inserts what we specified at the specified coordinates
        card_computer_txt.insert('4.22', '-') # Inserts what we specified at the specified coordinates

    else: # Otherwise
        for figure_with_bag in range(randint(0, 90)): # The bag goes through the cycle
            bag_lbl = Label(bag_frm, width=30, text="{}".format(figure_with_bag)) # Makes a bag
            bag_lbl.grid(padx=5, pady=5, row=2, column=0) # Closes the bag and puts it in the place we indicated

    if computer_card_num1 == '-' and computer_card_num2 == '-' and computer_card_num3 == '-' and computer_card_num4 == '-' and computer_card_num5 == '-' and computer_card_num6 == '-' and computer_card_num7 == '-' and computer_card_num8 == '-' and computer_card_num9 == '-' and computer_card_num10 == '-' and computer_card_num11 == '-' and computer_card_num12 == '-' and computer_card_num13 == '-' and computer_card_num14 == '-' and computer_card_num15 == '-': #  If the variable is "-"
        messagebox.showinfo('WIN!', 'Computer WIN!') # Sends a message that computer win
        root.destroy() # Closes the main window
        win_computer = Tk() # Creates a new window
        win_computer.title("Computer win") # Name this window as we specified
        win_lbl = Label(win_computer, width=30, text="COMPUTER WIN") # It says that you win
        win_lbl.pack() # Closes the label
        win_computer.mainloop() # # Closes the program


def bag_menu(): # Makes a function
    
    global figure_with_bag # Declare these variables in a function
    bag_lbl = Label(bag_frm, width=30, text="{}".format(figure_with_bag)) # Make a bag
    bag_lbl.grid(padx=5, pady=5, row=2, column=0) # Closes the bag

    bag_lbl_lbl = Label(bag_frm, width=30, text="New barrel:") # Makes a name for the bag
    bag_lbl_lbl.grid(padx=5, pady=5, row=1, column=0) # Closes the name of the bag
    delete_btn = Button(bag_frm, width=30,
                        text="Cross out the number", command=delete_loto) # Makes a delete button
    delete_btn.grid(padx=5, pady=5, row=3, column=0) # Closes the delete button

    continue_btn = Button(
        bag_frm, width=30, text="Continue", command=continue_loto) # Makes a continue button that once again throws the bag
    continue_btn.grid(padx=5, pady=5, row=4, column=0) # Closes the continue button, which once again throws the bag
    

player_lbl = Label(player_frm, width=30, text="Player menu") # Makes the player's name
player_lbl.grid(padx=5, pady=5, row=0, column=0) # Closes the player's name


Bag_btn = Button(bag_frm, width=30,
                 text="Throw the mouse", command=bag_menu) # Makes a one-time bag button that starts the bag
Bag_btn.grid(padx=5, pady=5, row=3, column=0) # Closes a one-time bag button that starts the bag

computer_lbl = Label(computer_frm, width=30, text="Computer menu") # Makes the computer name
computer_lbl.grid(padx=5, pady=5, row=0, column=0) # Closes the computer name

logger.info("Everything is good") # Добавляє лог який каже що функція відпрацювала  

root.mainloop() # Closes the program
