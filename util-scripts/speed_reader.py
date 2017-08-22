import subprocess
import time
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *

from itertools import izip_longest


class Fullscreen_Window:

    def __init__(self, data):
        self.tk = Tk()
        # self.tk.attributes('-zoomed', True)
        self.tk.attributes('-fullscreen', True)
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    # print data
    return data

def printToScreen(w, data):
    text_widget = Text(w.tk)
    text_widget.tag_configure('center', justify='center')
    text_widget.insert("1.0", data)
    text_widget.tag_add("center", "1.0", "end")
    text_widget.pack()


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def main():
    data = getClipboardData()
    for i in grouper(data.split(' '), 3, 'x'):
        print " ".join(i)
        time.sleep(0.5)


    # Print multiple time
    # w = Fullscreen_Window(data)
    # for word in data.split(' '):
    #     printToScreen(w, word)

    # Center justified screen text
    #    w.tk.config(height=500, width=500)
    #    can = Canvas(w.tk, height=100, width=100)
    #    can.pack(side="top", fill='both', expand=True)
    #    canvas_id = can.create_text(10, 10, anchor='nw')
    #    can.itemconfig(can, text=data)
    #    can.insert(canvas_id, len(data), data)
    #    can.place(relx=0.5, rely=0.5, anchor=CENTER)

    # MAIN LOOP 
    # w.tk.mainloop()


if __name__ == '__main__':
    main()
