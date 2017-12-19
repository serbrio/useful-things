# -*- coding: utf-8 -*-


##
##Just for fun
##

"""
...
"""

from Tkinter import *
import tkFileDialog
import ttk
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
    if count == '-':
        txt = ''
    else:
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
        #end_idx = textbox.index(CURRENT)
        end_idx = start_idx.split('.')[0] + '.' + str(len(i[0]))
        textbox.tag_add('keyWord', start_idx, end_idx)
        textbox.tag_config('keyWord', background="#BFFFD2", foreground="black")
        textbox.insert(END, i[1])
        textbox.insert(END, '\n')
        textbox.insert(END, '  ')
        textbox.insert(END, '\n')
    ResultText(ent, n)


root = Tk()
root.title('Nederlands-Russisch Woordenboek')
#root.geometry('1000x1000')
textVar = StringVar()

nb = ttk.Notebook(root)
nb.pack(side='top', fill='both', expand=1)

page1 = ttk.Frame(nb)
nb.add(page1, text='Search in dictionary')


searchboxFrame = Frame(page1)
panelFrame = Frame(page1, height=60, bg='gray')
textFrame = Frame(page1, height=340, width=600)

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
findBtn.place(relx=0.0, x=10, rely=0.0, y=10, width=80, height=40)
saveBtn.place(relx=1.0, x=-140, rely=0.0, y=10, width=80, height=40)
quitBtn.place(relx=1.0, x=-50, rely=0.0, y=10, width=40, height=40)


page2 = ttk.Frame(nb)
nb.add(page2, text='Experiment')
Zaglushka = Label(page2, text='Denk aleer gij doende zijt en doende denk dan nog. \n '
                              'Een goed begin is het halve werk. \n '
                              'Een goed verstaander heeft maar een half woord nodig. \n'
                              'Een half ei is beter dan een lege dop.', font='Arial 20', bg="#FFCC99", fg='black')
Zaglushka.pack(side=TOP, expand=1, fill='both')

root.mainloop()


