# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

from Tkinter import *
import tkFileDialog
import dict_creator


def Quit(ev):
    global root
    root.destroy()


def LoadFile(ev):
    fn = tkFileDialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write((textbox.get('1.0', 'end')).encode('utf-8'))

def ResultText(request, count):
    txt = 'Found ' + str(count) + ' matches for "' + request + '".'
    textVar.set(txt)

def Find(ev):
    textbox.delete('1.0', END)
    ent = (searchbox.get()).encode('utf-8')
    result, n = dict_creator.d_searcher(ent, dict_creator.d_creator())
    #textbox.tag_config("keyWord", background="yellow", foreground="blue")
    for i in result:
        start_idx = textbox.index(CURRENT)
        textbox.insert(END, i[0])
        textbox.insert(END, '\n')
        end_idx = textbox.index(CURRENT)
        textbox.tag_add('keyWord', start_idx, end_idx)
        textbox.tag_config('keyWord', background="#BFFFD2", foreground="black")
        textbox.insert(END, i[1])
        textbox.insert(END, '\n')
        textbox.insert(END, '  ')
        textbox.insert(END, '\n')
    ResultText(ent, n)


root = Tk()
textVar = StringVar()

searchboxFrame = Frame(root)
panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=600)

searchboxFrame.pack(side='top', fill='both')
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)


searchInvitation = Label(searchboxFrame, text="Search: ", font='Arial 14')
searchbox = Entry(searchboxFrame, bd=10, fg='blue', cursor='arrow', font='Arial 14')
searchInvitation.pack(side=LEFT)
searchbox.pack(side=RIGHT, fill='both', expand=1)
searchbox.bind("<KeyRelease>", Find)

resultSum = Label(textFrame, textvariable=textVar, fg='blue', cursor='dot')
resultSum.pack(side=BOTTOM, fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)


scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

#loadBtn = Button(panelFrame, text='Load')
saveBtn = Button(panelFrame, text='Save to file')
quitBtn = Button(panelFrame, text='Quit')
findBtn = Button(panelFrame, text='Find')

#loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)
findBtn.bind("<Button-1>", Find)


#loadBtn.place(x=10, y=10, width=40, height=40)
findBtn.place(x=10, y=10, width=40, height=40)
saveBtn.place(x=760, y=10, width=80, height=40)
quitBtn.place(x=850, y=10, width=40, height=40)

root.mainloop()


