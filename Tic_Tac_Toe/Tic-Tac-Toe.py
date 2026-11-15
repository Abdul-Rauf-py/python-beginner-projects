import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("366x355")

buttons = []
current_player = "X"

def on_click(square):
    
    global current_player
    if current_player == "X":
        buttons[square].config(text = current_player , bg = "pink" , fg = "black" , font = ('Arial' , 9) , state = "disabled")
    else:
        buttons[square].config(text = current_player , bg = 'lightblue' , fg = "black" , font = ('Arial' , 9) , state = "disabled")    
        

    
    if (buttons[0]["text"] == current_player and
        buttons[1]["text"] == current_player and
        buttons[2]["text"] == current_player) or (buttons[0]["text"] == current_player and
        buttons[3]["text"] == current_player and
        buttons[6]["text"] == current_player) or (buttons[0]["text"] == current_player and
        buttons[4]["text"] == current_player and
        buttons[8]["text"] == current_player) or (buttons[1]["text"] == current_player and
        buttons[4]["text"] == current_player and
        buttons[7]["text"] == current_player) or (buttons[2]["text"] == current_player and
        buttons[4]["text"] == current_player and
        buttons[6]["text"] == current_player) or (buttons[2]["text"] == current_player and
        buttons[5]["text"] == current_player and
        buttons[8]["text"] == current_player) or (buttons[3]["text"] == current_player and
        buttons[4]["text"] == current_player and
        buttons[5]["text"] == current_player) or (buttons[6]["text"] == current_player and
        buttons[7]["text"] == current_player and
        buttons[8]["text"] == current_player):
        
        output_label.config(text=f"{current_player} wins!" , font = ('Arial' , 14))
                
        for button in buttons:
            button.config(state="disabled")
        return
     
    filled = 0
    for button in buttons:
        if button["text"] != "":
            filled += 1
    if filled == 9:
        output_label.config(text="It's a draw!")
        return
    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def on_reset_game():
    global current_player
    for button in buttons:
        button.config(text="" , state = "normal" , bg = "white" )
    output_label.config(text="")
    current_player = "X"

# for i in range(1,10):
#     row = (i - 1) // 3
#     column = (i - 1) % 3
#     button = tk.Button(root , text = "" , width = 16 , height = 6 , command = lambda : on_click(i))
#     button.grid(row = row , column = column)


button1 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(0))
button1.grid(row = 0 , column = 0)
buttons.append(button1)
button2 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(1))
button2.grid(row = 0 , column = 1)
buttons.append(button2)
button3 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(2))
button3.grid(row = 0 , column = 2)
buttons.append(button3)
button4 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(3))
button4.grid(row = 1 , column = 0)
buttons.append(button4)
button5 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(4))
button5.grid(row = 1 , column = 1)
buttons.append(button5)
button6 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(5))
button6.grid(row = 1 , column = 2)
buttons.append(button6)
button7 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(6))
button7.grid(row = 2 , column = 0)
buttons.append(button7)
button8 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(7))
button8.grid(row = 2 , column = 1)
buttons.append(button8)
button9 = tk.Button(root , text = "" , width = 16 , height = 6 , bg = 'white' , command = lambda : on_click(8))
button9.grid(row = 2 , column = 2)
buttons.append(button9)

play_again=tk.Button(root , text="Reset Game." , command = on_reset_game )
play_again.grid(row=4, column=0, columnspan=3)

output_label=tk.Label(root , text="")
output_label.grid(row=3, column=0, columnspan=3)
root.mainloop()
