from tkinter import *

win = Tk()
win.geometry('1000x500')

win.title('temp')
win.option_add('*Font','맑은고딕 25')

btn = Button(win, text='버튼')
btn.pack()


win.mainloop()