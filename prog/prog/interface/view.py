#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" View
"""

         
from math import *
from tkinter import *

import model
import parameters


#----------------- data ------------------------
nc = parameters.NC
nl = parameters.NL
mortality =parameters.MORTALITY
cell_size = parameters.CELL_SIZE

pandemia = model.create_board(nc, nl)
states_colors = {"sick":"orange red", "healthy":"linen", "touched":"dark grey", "immune":"SkyBlue1"}
states_names = {"sick":"Infectée", "healthy":"Saine", "touched":"Touchée", "immune":"Immunisée"}

#----------------- callbacks ------------------------

def set_cell_color(l, c, color):
    ident = grid[c][l]
    canvas.itemconfigure(ident, fill=color)

def draw_grid():
    for l in range(nl):
        for c in range(nc):
                color = states_colors[model.get_cell(pandemia, l, c)]
                set_cell_color(l, c, color)

def healthy_board():
    model.healthy_board(pandemia, nc, nl)
    draw_grid()
    
def random_board():
    immunePercent=immuneVal.get()
    model.random_board(pandemia, nc, nl, immunePercent)
    draw_grid()

def edit_grid(event):
    state = cell_type.get()
    c = (event.x-1)//cell_size
    l = (event.y-1)//cell_size
    model.set_cell(pandemia, l, c, state)
    color = states_colors[state]
    set_cell_color(l, c, color)
   

def compute_evolution():
    if pause.get() == 0 :
        res = model.compute_step(pandemia, nc, nl)
        draw_grid()
        speed = speedVal.get()
        final_result.configure(text = "Résultat : " + str(round(model.compute_stats(pandemia, nc, nl, mortality),2)) + "% de mortalité")
        if speed > 0 and res:
            delay = 1000 * speed #  ms
            window.after(delay, compute_evolution)
        else:
            pause.set(1)

def switch_pause():
    if pause.get() == 1:
        pause.set(0)
        compute_evolution()
    else:
        pause.set(1)

def get_prevision():
    return (100-immuneVal.get())*mortality//100
        
#----------------- interface ------------------------

window = Tk()
window.title("Pandémie")
window.columnconfigure(0, weight=2)
window.rowconfigure(0, weight=1)

## MAP
canvas = Canvas(window, width=nc*cell_size, height=nl*cell_size,
                background="black", highlightbackground="black")

grid = [None]*nc
for i in range (0, nc):
    grid[i] = [None]*nl
        
for l in range(nl):
    for c in range(nc):
        top_x = c*cell_size+1
        top_y = l*cell_size+1
        # creates the square
        grid[c][l] = canvas.create_rectangle(top_x, top_y, top_x + cell_size, top_y + cell_size,
                                             fill="grey", activefill="black")

healthy_board()
canvas.grid(column=0, row=0)
canvas.bind('<Button-1>', edit_grid)

## COMMANDS
frame = Frame(window)
frame.grid(column=1, row=0, sticky="nsew")

## Edition
edition = LabelFrame(frame, bd=4, text="Édition")
edition.grid(row=0, sticky="ew", pady=10, ipady=10, padx=10, ipadx=10)
edition.columnconfigure(0, weight=1)
edition.columnconfigure(1, weight=1)
# clear map button
clearmap_button = Button(edition, text="Init",
                         highlightbackground="grey", anchor='center',
                         command=healthy_board)
clearmap_button.grid(column=0, row=1, ipadx=10, ipady=5, padx=10, pady=10)
# selection of the cell type in the edition
cell_type = StringVar()
i=0
for state in states_colors:
    if state != "touched":
        color = states_colors[state]
        name = states_names[state]
        button = Radiobutton(edition, variable=cell_type, text=name, value=state, background=color)
        button.grid(column=1, row=i, sticky="w", padx=30)
        i = i+1
button.select()

## Generation
generation = LabelFrame(frame, bd=4, text="Génération")
generation.grid(row=1, column = 0, sticky="ew", pady=10, ipady=10, padx=10, ipadx=10)
generation.columnconfigure(0, weight=1)
generation.columnconfigure(1, weight=1)

# random Map Button
random_button = Button(generation, text="Carte Aléatoire",
                       highlightbackground="grey", anchor='center',
                       command=random_board)
random_button.grid(row=0, column=0, ipadx=10, ipady=5, padx=10, pady=10)

# parameter (immunune percentage)
immuneVal = IntVar(value=0)
immune_percent = Scale(generation, orient="horizontal", variable=immuneVal, from_=0, to=100, tickinterval=10,
                    length=300, label="Population vaccinée (% population totale)")
immune_percent.grid(row=1, columnspan=3)


## Control
speedVal = IntVar(value=0)
control = LabelFrame(frame, bd=4, text="Contrôle")
control.grid(row=2, column=0, sticky="ew", pady=10, ipady=10, padx=10, ipadx=10)
control.columnconfigure(0, weight=1)
control.columnconfigure(1, weight=1)
control.columnconfigure(2, weight=1)
# speed scale
speed_scale = Scale(control, orient="horizontal", variable=speedVal, from_=0, to=5, tickinterval=1,
                    length=300, label="Nombre de secondes entre chaque pas")
speed_scale.grid(row=0, columnspan=3)
# pause button
pause = BooleanVar()
pause.set(1)
bpause = Button(control, text="On/Off", command=switch_pause)
bpause.grid(row=1, column=0)
# quit button
bquit = Button(control, text="Quitter", command=window.destroy)
bquit.grid(row=1, column=2)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

result = LabelFrame(frame, bd=4, text="Bilan")
result.grid(row=3, column=0, sticky="ew", pady=10, ipady=10, padx=10, ipadx=10)
mortalityTxt= Label(result, bd = 4, text = str(mortality) + "% de mortalité dans la population touchée")
mortalityTxt.grid(row=0)
        
#prevision= Label(result, bd = 4, text = "Prévision : " + str(get_prevision()) + "% de mortalité")
#prevision.grid (row = 0)
final_result= Label(result, bd = 4, text = "Résultat : " + str(round(model.compute_stats(pandemia, nc, nl, mortality), 2)) + "% de mortalité totale")
final_result.grid (row = 1)

           
window.mainloop()


            



     
   
            
   
        

    
