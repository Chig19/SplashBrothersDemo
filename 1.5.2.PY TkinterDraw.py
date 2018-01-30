""" TkinterDraw.py demonstrates some methods of Tkinter.Canvas
Revision 10/29/2013 Copyright 2013 PLTW
"""
from Tkinter import *          #don't import like this except for Tkinter
root = Tk()                      #create main window

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.grid() #Puts the canvas in the main Tk window

# Make four objects on the canvas
checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4])
check = canvas.create_line(100,200,150,250,100,300,200,200,150,250,200,300, fill='red', width=20)
message = canvas.create_text(350, 500, text='Youssaf Ahmed has a bomb', font=('Wingdings', 20))


# Make an array of objects on the canvas
circles=[]
for r in range(10, 60, 10):
    circles += [canvas.create_oval(300-r, 400-r, 300+r, 400+r, outline='red')]

# Make one more object on the canvas
canopy = canvas.create_arc(0, 50, 600, 650, outline='green',  fill='green', start=30, extent=120, 
                           width=50, style=ARC) 

# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.
root.mainloop() 