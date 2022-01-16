from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title( 'Button Example' )
def dialog() :
    var = box.askyesno( 'Message Box' , 'Processed?' )
    if var == 1 :
        box.showinfo( 'Yes Box' , 'Processing...' )
    else :
        box.showwarning( 'No Box' , 'Cancelling...' )
btn = Button( window , text = 'Click' , command=dialog )
btn.pack( padx = 150 , pady = 50 )
window.mainloop()