# pip install tkinterscrolledframe
# pip install tkinter if you do not have it installed
# pip install pandas if you do not have it installed

from datetime import datetime
from tkscrolledframe import ScrolledFrame
import tkinter as tk
import math
import pandas as pd
import tkinter.font as tkfont
# encoding


def encode(txt, key, skey, lkey):
    rkey = 1
    for i in range(rkey):
        # txt = shift(txt, key, skey)
        txt = shiftLetter(list(txt), key, lkey)
    return ''.join(txt)


def shift(txt, key, skey):
    txt = list(txt)
    encoded_txt = txt.copy()

    idx = skey-len(txt)*math.floor(skey/len(txt))
    for i in range(len(txt)):
        encoded_txt[i] = txt[idx]
        idx += 1
        if(idx >= len(txt)):
            idx = 0
    return encoded_txt


def shiftLetter(txt, key, lkey):
    encoded_txt = txt.copy()

    for i in range(len(txt)):
        idx = key.index(encoded_txt[i])+lkey
        idx = idx-len(key)*math.floor(idx/len(key))
        encoded_txt[i] = key[idx]
    return encoded_txt


def toBinary(string):
    return' '.join(format(x, 'b') for x in bytearray(string, 'utf-8'))


def encodeBinary(binaryString, key):
    binaryStringLst = binaryString.split(' ')

    for i in range(len(binaryStringLst)):
        binaryStringLst[i] = list(binaryStringLst[i])
        for j in range(len(binaryStringLst[i])):
            binaryStringLst[i][j] = key[int(binaryStringLst[i][j])]
        binaryStringLst[i] = ''.join(binaryStringLst[i])
    return ' '.join(binaryStringLst)


def decode_encoded_Binary(binary_string, key):
    encodedbinaryStringLst = binary_string.split(' ')
    for i in range(len(encodedbinaryStringLst)):
        encodedbinaryStringLst[i] = list(encodedbinaryStringLst[i])
        for j in range(len(encodedbinaryStringLst[i])):
            encodedbinaryStringLst[i][j] = str(
                key.index(encodedbinaryStringLst[i][j]))
        encodedbinaryStringLst[i] = ''.join(encodedbinaryStringLst[i])
    return ' '.join(encodedbinaryStringLst)


def decodeBinary(binary_string):
    encodedbinaryStringLst = binary_string.split(' ')
    fromBinaryStringLst = [chr(int(x, 2)) for x in encodedbinaryStringLst]
    return ''.join(fromBinaryStringLst)

# list of characters
# chars = 'abcdefghijklmnopqrstuvwxyz 1234567890-:|,'
# chars = 'abcdefghijklmnopqrstuvwxyz'
# symbols = """!@#$%^&*()/\\_+| \n\t"""
# numbers = '1234567890'
# chars += chars.upper() + numbers + symbols


# topRow = '`1234567890-='
# sTopRow = '~!@#$%^&*()_+'
# sideSyms = "[]\\;',./"
# sSideSyms = '{}|:"<>?'


# extraChars = topRow+sTopRow+sideSyms+sSideSyms
# saveChars = ''.join(set(chars+extraChars))
# chars = saveChars

# letters = 'abcdefghijklmnopqrstuvwxyz'
# sletters = letters.upper()
# topRow = '`1234567890-='
# sTopRow = '~!@#$%^&*()_+'
# sideSyms = "[]\\;',./"
# sSideSyms = '{}|:"<>?'
# escapes = '\n\t '
# extraChars = topRow+sTopRow+sideSyms+sSideSyms
# saveChars = extraChars + letters + sletters + escapes
# chars = saveChars

# FULL LIST OF CHARS
# keys = {
#     'letters': 'abcdefghijklmnopqrstuvwxyz',
#     'sletters': 'abcdefghijklmnopqrstuvwxyz'.upper(),
#     'topRow': '`1234567890-=',
#     'sTopRow': '~!@#$%^&*()_+',
#     'sideSyms': "[]\\;',./",
#     'sSideSyms': '{}|:"<>?',
#     'escapes': '\n\t '
# }
# saveChars = ''.join(list(keys.values()))
# chars = saveChars
#   
# unordered list of Chars
saveChars = """`r9R* Dm@p(2[Iz>x)^tqjOL6SME"8?}o|!C]A$-+X4NFdP:/f3KGJvT0laBw%~W\'bUgks,Hui\t\\Y#e_7&Z{VQ;cn5.=<\nh1y"""
chars = saveChars
replacementChars = ['\'','"']
#  TESTING DATAFRAME
# testData = [
#     [encode(datetime.today().strftime('%m/%d/%y'), chars, 43322, 233), encode('testing1', chars, 43322, 233), encode('ducks', chars, 43322, 233)],
#     [encode(datetime.today().strftime('%m/%d/%y'), chars, 43322, 233), encode('testing2', chars, 43322, 233), encode('ducks rule', chars, 43322, 233)],
#     [encode(datetime.today().strftime('%m/%d/%y'), chars, 43322, 233), encode('testing3', chars, 43322, 233), encode('ducks are best', chars, 43322, 233)],
#     [encode(datetime.today().strftime('%m/%d/%y'), chars, 43322, 233), encode('testing4', chars, 43322, 233), encode('plop', chars, 43322, 233)],
# ]
# df = pd.DataFrame(
#     testData,
#     columns=['date', 'title','text']
# )
# df.to_csv('textEntry.csv', encoding='utf-8', index=False)

# print(len(df.columns))

# for i in range(len(df)):
#     for j in df.columns:
#         df.loc[i, j] = encode(df.loc[i, j], chars, -43322, -233)
#     # df.loc[i, 'date'] = encode(df.loc[i, 'date'], chars, -43322, -233)
#     # df.loc[i, 'title'] = encode(df.loc[i, 'title'], chars, -43322, -233)
#     # df.loc[i, 'text'] = encode(df.loc[i, 'text'], chars, -43322, -233)
# print(df)

# date = datetime.today().strftime('%m/%d/%Y')
# time = datetime.strptime(datetime.today().strftime('%H:%M'), "%H:%M").strftime('%r')
# print(date+', '+time)

# quit()

# import subprocess
# from random import randint
# new_txt = []
# odr = list(saveChars).copy()
# for i in range(len(odr), 0, -1):
#   idx = randint(0, len(odr)-1)
#   new_txt.append(odr[idx])
#   odr.pop(idx)
# new_txt = ''.join(new_txt)
# print(new_txt)

# def copy2clip(txt):
#     cmd='echo '+txt+'|clip'
#     return subprocess.check_call(cmd, shell=True)
# copy2clip(repr(str(new_txt)))
# quit()

#  END TESTING SEQUENCE
# Tkinter


def getCurrentEncoding():
    skeyNum = int(skey.get('1.0', tk.END))
    lkeyNum = int(lkey.get('1.0', tk.END))
    return (skeyNum, lkeyNum)


def runKey():
    pass


def saveTxt(skip=False):
    skey, lkey = getCurrentEncoding()
    if(prev_values[0] == -skey and prev_values[1] == -lkey):
        skip = True
    else:
        PopOut2(window)
        return

    if(skip):
        print('saving anyway')
        skey, lkey = getCurrentEncoding()
        df2 = df.copy()
        print('Saved')
        for i in range(len(df)):
            for j in df.columns:
                data = df2.loc[i, j]
                encoded_data = encode(data, saveChars, skey, lkey)
                binary_encoded_data = toBinary(encoded_data)
                encoded_binary_encoded_data = encodeBinary(
                    binary_encoded_data, saveChars)
                encoded_binary_encoded_data = encoded_binary_encoded_data.replace('`', '\'')
                encoded_binary_encoded_data = encoded_binary_encoded_data.replace('r', '"')
                df2.loc[i, j] = encoded_binary_encoded_data
                # df2.loc[i, j] = encode(df2.loc[i, j], saveChars, skey, lkey)
        df2.to_csv(filename, encoding='utf-8', index=False)
        saved_lbl.configure(text='Document Saved', bg='#0a0', )
        return


def readText(idx):
    pass


def readCSV():
    pass


def autosave_to_df(a):
    saved_lbl.configure(text='*Unsaved Document', bg='#a00', )

    df.loc[currentEntry, 'text'] = txt_edit.get('1.0', tk.END)
    df.loc[currentEntry, 'last_updated'] = datetime.today().strftime('%m/%d/%y')
    scrolledfrm.winfo_children()[currentEntry].winfo_children()[-1].configure(text=df.loc[currentEntry,'last_updated'])
    # for i in scrolledfrm.winfo_children():
    #     # print(i)
    #     i.destroy()
    # for i in range(len(df)):
    #     # date = str(df.loc[i, 'date'].strip('\n'))
    #     # new_title = str(df.loc[i, 'title']).strip('\n')
    #     # btn_txt = date+'\n'+new_title
    #     # el = tk.Button(scrolledfrm, text=btn_txt,
    #     #                command=lambda x=i: changeEntry(x))
    #     # el.pack()
    #     # btn_frm = tk.Frame(scrolledfrm, bg='#bbb', width=100, height=100, relief=tk.RAISED, border=2)
    #     # btn_frm.pack(side="top", fill="x", expand=False, pady=5)
    #     # btn_frm.bind('<Button-1>', lambda x=i: changeEntry(x))

    #     # title = tk.Label(btn_frm, text=str(df.loc[i, 'title']).strip('\n'),width=10, bg='#ddd')
    #     # title.pack(anchor=tk.CENTER, expand=True, fill=tk.X, side='top', ipadx=2)
    #     # title.configure(font=('Arial', 10))

    #     # date = tk.Label(btn_frm, text='Date Created: '+str(df.loc[i, 'date']).strip('\n'), bg='#ddd')
    #     # date.pack(anchor=tk.CENTER, expand=True, fill=tk.X, side='top', ipadx=2)
    #     # date.configure(font=('Arial', 7))

    #     # last_updated = tk.Label(btn_frm, text='Last Updated: '+str(df.loc[i, 'last_updated']).strip('\n'), bg='#ddd')
    #     # last_updated.pack(anchor=tk.CENTER, expand=True, fill=tk.X, side='top', ipadx=2)
    #     # last_updated.configure(font=('Arial', 7))
    #     btn_frm = tk.Frame(scrolledfrm, bg='#bbb', width=100, height=100, relief=tk.RAISED, border=2)
    #     btn_frm.pack(side="top", fill="x", expand=False, pady=2)
    #     btn_frm.bind('<Button-1>', lambda y,x=i: changeEntry(x))

    #     title = tk.Label(btn_frm, text=str(df.loc[i, 'title']).strip('\n'), bg='#ddd', width=10)
    #     title.grid(row=0, column=0, sticky='nsew')
    #     title.configure(font=('Arial', 10))
    #     title.bind('<Button-1>', lambda y,x=i: changeEntry(x))

    #     date = tk.Label(btn_frm, text=str(df.loc[i, 'date']).strip('\n'), bg='#ddd', width=7)
    #     date.grid(row=0, column=1, sticky='nsew')
    #     date.configure(font=('Arial', 7))
    #     date.bind('<Button-1>', lambda y,x=i: changeEntry(x))

    #     last_updated = tk.Label(btn_frm, text=str(df.loc[i, 'last_updated']).strip('\n'), bg='#ddd', width=7)
    #     last_updated.grid(row=0, column=2, sticky='nsew')
    #     last_updated.configure(font=('Arial', 7))
    #     last_updated.bind('<Button-1>', lambda y,x=i: changeEntry(x))




def autosave_title_to_df(a):
    global df
    df.loc[currentEntry, 'title'] = title.get('1.0', tk.END)
    
    # df.loc[currentEntry, 'last_updated'] = datetime.today().strftime('%m/%d/%y')

    # for i in scrolledfrm.winfo_children():
    #     i.destroy()
    # for i in range(len(df)):
    #     el = tk.Button(scrolledfrm, text=str(df.loc[i, 'title']).strip('\n'), command=lambda x=i:changeEntry(x))
    #     el.pack()
    saved_lbl.configure(text='*Unsaved Document', bg='#a00', )
    scrolledfrm.winfo_children()[currentEntry].winfo_children()[0].configure(text=df.loc[currentEntry,'title'].strip('\n'))


    # for i in scrolledfrm.winfo_children():
    #     i.destroy()
    # for i in range(len(df)):
    #     date = str(df.loc[i, 'date'].strip('\n'))
    #     new_title = str(df.loc[i, 'title']).strip('\n')
    #     btn_txt = date+'\n'+new_title
    #     el = tk.Button(scrolledfrm, text=btn_txt,
    #                    command=lambda x=i: changeEntry(x))
    #     el.pack()


def search(a):
    df2 = df
    typ = str(searchBar.get('1.0', tk.END)).strip('\n')
    if(len(typ) < 2):
        for i in scrolledfrm.winfo_children():
            i.destroy()
        for i in range(len(df)):
            createBtns(i)
        return

    Search = typ[1:]
    typ = typ[0]

    pattern = str(Search)
    if(typ == 'd'):
        # .reset_index(drop=True)
        df2 = df[df['date'].str.contains(fr'{pattern}')]
    elif typ == 't':
        # .reset_index(drop=True)
        df2 = df[df['title'].str.contains(fr'{pattern}')]
    elif typ == 'l':
        # .reset_index(drop=True)
        df2 = df[df['title'].str.contains(fr'{pattern}')]


    for i in scrolledfrm.winfo_children():
        i.destroy()

    indices = df2.index.tolist()
    print(indices)

    for i in range(len(df2)):
        # date = str(df2.loc[indices[i], 'date'].strip('\n'))
        # new_title = str(df2.loc[indices[i], 'title']).strip('\n')
        # btn_txt = date+'\n'+new_title

        # el = tk.Button(scrolledfrm, text=btn_txt,
        #                command=lambda x=indices[i]: changeEntry(x))
        # el.pack()
        createBtns(indices[i])

def changeEntry(index):
    global currentEntry,df

    txt_edit.delete('1.0', tk.END)  
    txt_edit.insert('1.0', str(df.loc[index, 'text']))
    title.delete('1.0', tk.END)
    title.insert('1.0', str(df.loc[index, 'title']))

    scrolledfrm.winfo_children()[currentEntry].configure(bg='#bbb', padx=0, pady=2)
    currentEntry = index
    scrolledfrm.winfo_children()[currentEntry].configure(bg='#a00', padx=2, pady=2)


def delete():
    global currentEntry, df
    if(currentEntry == False):
        return
    df = df.drop(index=currentEntry).reset_index(drop=True)

    txt_edit.delete('1.0', tk.END)
    title.delete('1.0', tk.END)
    currentEntry = False
    saved_lbl.configure(text='*Unsaved Document', bg='#a00', )

    for i in scrolledfrm.winfo_children():
        i.destroy()
    for i in range(len(df)):
        date = str(df.loc[i, 'date'].strip('\n'))
        new_title = str(df.loc[i, 'title']).strip('\n')
        btn_txt = date+'\n'+new_title
        el = tk.Button(scrolledfrm, text=btn_txt,
                       command=lambda x=i: changeEntry(x))
        el.pack()


def add():
    global currentEntry, df
    data = {
        'date': datetime.today().strftime('%m/%d/%y'),
        'title': 'Title',
        'text': 'Enter your text here.'
    }
    data = pd.DataFrame.from_dict(data, orient='index').T
    
    # deprecated as of pandas -v 1.4.0 January 22 2022
    # df = df.append(data, ignore_index=True)
    # instead
    df = pd.concat([df,data], ignore_index=True)
    print(df)

    txt_edit.delete('1.0', tk.END)
    txt_edit.insert('1.0', df.loc[len(df.index)-1, 'text'])
    title.delete('1.0', tk.END)
    title.insert('1.0', df.loc[len(df.index)-1, 'title'])
    
    
    scrolledfrm.winfo_children()[currentEntry].configure(bg='#bbb', padx=0, pady=2)
    currentEntry = len(df.index)-1

    saved_lbl.configure(text='*Unsaved Document', bg='#a00', )

    for i in scrolledfrm.winfo_children():
        i.destroy()
    for i in range(len(df)):
        # date = str(df.loc[i, 'date'].strip('\n'))
        # new_title = str(df.loc[i, 'title']).strip('\n')
        # btn_txt = date+'\n'+new_title
        # el = tk.Button(scrolledfrm, text=btn_txt,
        #                command=lambda x=i: changeEntry(x))
        # el.pack()
        btn_frm = tk.Frame(scrolledfrm, bg='#bbb', width=100, height=100, relief=tk.RAISED, border=2)
        btn_frm.pack(side="top", fill="x", expand=False, pady=2)
        btn_frm.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        titlelbl = tk.Label(btn_frm, text=str(df.loc[i, 'title']).strip('\n'), bg='#ddd', width=10)
        titlelbl.grid(row=0, column=0, sticky='nsew')
        titlelbl.configure(font=('Arial', 10))
        titlelbl.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        date = tk.Label(btn_frm, text=str(df.loc[i, 'date']).strip('\n'), bg='#ddd', width=7)
        date.grid(row=0, column=1, sticky='nsew')
        date.configure(font=('Arial', 7))
        date.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        last_updated = tk.Label(btn_frm, text=str(df.loc[i, 'last_updated']).strip('\n'), bg='#ddd', width=7)
        last_updated.grid(row=0, column=2, sticky='nsew')
        last_updated.configure(font=('Arial', 7))
        last_updated.bind('<Button-1>', lambda y,x=i: changeEntry(x))

    scrolledfrm.winfo_children()[currentEntry].configure(bg='#a00', padx=2, pady=2)


def openCSV():
    PopOut1(window)


def setupFrame():
    for i in scrolledfrm.winfo_children():
        i.destroy()
    for i in range(len(df)):
        # date = str(df.loc[i, 'date'].strip('\n'))
        # new_title = str(df.loc[i, 'title']).strip('\n')
        # btn_txt = date+'\n'+new_title
        # el = tk.Button(scrolledfrm, text=btn_txt,
        #                command=lambda x=i: changeEntry(x))
        # el.pack()
        createBtns(i)

def createBtns(i):
        btn_frm = tk.Frame(scrolledfrm, bg='#bbb', width=100, height=100, relief=tk.RAISED, border=2)
        btn_frm.pack(side="top", fill="x", expand=False, pady=2)
        btn_frm.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        title = tk.Label(btn_frm, text=str(df.loc[i, 'title']).strip('\n'), bg='#ddd', width=10)
        title.grid(row=0, column=0, sticky='nsew')
        title.configure(font=('Arial', 10))
        title.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        date = tk.Label(btn_frm, text=str(df.loc[i, 'date']).strip('\n'), bg='#ddd', width=7)
        date.grid(row=0, column=1, sticky='nsew')
        date.configure(font=('Arial', 7))
        date.bind('<Button-1>', lambda y,x=i: changeEntry(x))

        last_updated = tk.Label(btn_frm, text=str(df.loc[i, 'last_updated']).strip('\n'), bg='#ddd', width=7)
        last_updated.grid(row=0, column=2, sticky='nsew')
        last_updated.configure(font=('Arial', 7))
        last_updated.bind('<Button-1>', lambda y,x=i: changeEntry(x))



class PopOut1(tk.Toplevel):
    def __init__(self, master, **kwargs):
        self.popup = tk.Toplevel()
        self.popup.geometry('400x300')
        self.grid_spacing = 10
        # popup.rowconfigure(1, minsize=800, weight=1)
        # popup.columnconfigure(1, minsize=800, weight=1)
        self.createElements(self.popup)
        self.popup.focus_set()
        self.popup.grab_set()
        self.popup.mainloop()
        # releasing on any other tkinter window, within this process, forces focus back to this window

    def createElements(self, popup):
        master_frm = tk.Frame(popup)
        master_frm.place(anchor='c', relx=.5, rely=.5)
        popup.title("Open")

        # create file open frame
        self.file_frm = tk.Frame(master_frm)
        self.file_lbl = tk.Label(self.file_frm, text='Enter filename: ')
        self.file_txt = tk.Text(self.file_frm, width=15, height=1)

        self.file_frm.pack(ipady=self.grid_spacing)
        self.file_lbl.grid(row=0, column=0)
        self.file_txt.grid(row=0, column=1)

        # create first frame and elements
        self.key1_frm = tk.Frame(master_frm)
        self.key1_lbl = tk.Label(self.key1_frm, text='Enter skey: ')
        self.key1_txt = tk.Text(self.key1_frm, width=15, height=1)

        self.key1_frm.pack(ipady=self.grid_spacing)
        self.key1_lbl.grid(row=0, column=0)
        self.key1_txt.grid(row=0, column=1)

        # create second frame and elements
        self.key2_frm = tk.Frame(master_frm)
        self.key2_lbl = tk.Label(self.key2_frm, text='Enter lkey: ')
        self.key2_txt = tk.Text(self.key2_frm, width=15, height=1)

        self.key2_frm.pack(ipady=self.grid_spacing)
        self.key2_lbl.grid(row=0, column=0)
        self.key2_txt.grid(row=0, column=1)

        self.B1 = tk.Button(master_frm, text="Open",
                            command=self.openCSV, width=20, height=1)
        self.B1.pack(ipady=self.grid_spacing)

    def createEntryButtons(self):
        for i in scrolledfrm.winfo_children():
            i.destroy()
        for i in range(len(df)):
            # date = str(df.loc[i, 'date'].strip('\n'))
            # title = str(df.loc[i, 'title']).strip('\n')
            # btn_txt = date+'\n'+title
            # el = tk.Button(scrolledfrm, text=btn_txt,
            #                command=lambda x=i: self.changeEntry(x))
            # el.pack()
            btn_frm = tk.Frame(scrolledfrm, bg='#bbb', width=100, height=100, relief=tk.RAISED, border=2)
            btn_frm.pack(side="top", fill="x", expand=False, pady=2)
            btn_frm.bind('<Button-1>', lambda y,x=i: changeEntry(x))

            title = tk.Label(btn_frm, text=str(df.loc[i, 'title']).strip('\n'), bg='#ddd', width=10)
            title.grid(row=0, column=0, sticky='nsew')
            title.configure(font=('Arial', 10))
            title.bind('<Button-1>', lambda y,x=i: changeEntry(x))

            date = tk.Label(btn_frm, text=str(df.loc[i, 'date']).strip('\n'), bg='#ddd', width=7)
            date.grid(row=0, column=1, sticky='nsew')
            date.configure(font=('Arial', 7))
            date.bind('<Button-1>', lambda y,x=i: changeEntry(x))

            last_updated = tk.Label(btn_frm, text=str(df.loc[i, 'last_updated']).strip('\n'), bg='#ddd', width=7)
            last_updated.grid(row=0, column=2, sticky='nsew')
            last_updated.configure(font=('Arial', 7))
            last_updated.bind('<Button-1>', lambda y,x=i: changeEntry(x))


    def openCSV(self):
        global df, filename, prev_values

        # get keys
        filename = (self.file_txt.get('1.0', tk.END).strip('\n'))
        skey = int(self.key1_txt.get('1.0', tk.END).strip('\n'))
        lkey = int(self.key2_txt.get('1.0', tk.END).strip('\n'))
        prev_values = [skey, lkey]

        # open file
        df = pd.read_csv(filename)
        print('Opened file')
        # print(df)
        # print(filename, skey, lkey)
        # decode file
        saved_lbl.configure(text='No Changes Made', bg='#aa0', fg='#000')

        for i in range(len(df)):
            for j in df.columns:
                df.loc[i, j] = df.loc[i,j].replace(replacementChars[0], '`')
                df.loc[i, j] = df.loc[i,j].replace(replacementChars[1], 'r')
                data = decodeBinary(decode_encoded_Binary(
                    df.loc[i, j], saveChars))  # decoded_data

                df.loc[i, j] = encode(data, chars, skey, lkey)

                # past encoding  use .txt instead
                # df.loc[i, j] = encode(df.loc[i, j], chars, skey, lkey)

        # fill text box with first entry
        txt_edit.delete('1.0', tk.END)
        txt_edit.insert('1.0', 'Enter text here')

        title.delete('1.0', tk.END)
        title.insert('1.0', 'Title')

        self.createEntryButtons()

        self.popup.destroy()

    def changeEntry(self, index):
        global currentEntry
        txt_edit.delete('1.0', tk.END)
        txt_edit.insert('1.0', df.loc[index, 'text'])
        title.delete('1.0', tk.END)
        title.insert('1.0', df.loc[index, 'title'])
        currentEntry = index


class PopOut2(tk.Toplevel):
    def __init__(self, master, **kwargs):
        self.popup = tk.Toplevel()
        self.popup.geometry('500x300')
        self.grid_spacing = 10
        # popup.rowconfigure(1, minsize=800, weight=1)
        # popup.columnconfigure(1, minsize=800, weight=1)
        self.createElements(self.popup)
        self.popup.focus_set()
        self.popup.grab_set()
        self.popup.mainloop()
        # releasing on any other tkinter window, within this process, forces focus back to this window

    def createElements(self, popup):
        master_frm = tk.Frame(popup)
        master_frm.place(anchor='c', relx=.5, rely=.5)
        popup.title("Save")

        self.warn_frm = tk.Frame(master_frm)
        self.warn_frm.pack(ipady=self.grid_spacing, fill=tk.X)

        self.file_warn = tk.Label(self.warn_frm, text='WARNING', bg='#f00')
        self.file_warn.configure(font=('Impact', 20))
        self.file_warn.pack(fill=tk.BOTH, anchor=tk.CENTER)

        # create file open frame
        self.file_frm = tk.Frame(master_frm)
        self.file_lbl = tk.Label(
            self.file_frm, text='Your current encoding values do not match past decoding values.\n Would you like to continue anyway?')
        self.file_lbl.configure(font=('Ariel', 12))
        self.file_frm.pack(ipady=self.grid_spacing)
        self.file_lbl.grid(row=1, column=0)

        # create first frame and elements
        self.key1_frm = tk.Frame(master_frm)
        self.key1_current_prev = tk.Label(
            self.key1_frm, text='Current, Previous')
        self.key1_current_prev.configure(font=('Times New Roman', 12))

        skey, lkey = getCurrentEncoding()
        self.key1_skey = tk.Label(
            self.key1_frm, text=f' {skey},   {-prev_values[0]}')
        self.key1_lkey = tk.Label(
            self.key1_frm, text=f' {lkey},   {-prev_values[1]}')
        self.key1_lkey.configure(font=('Times New Roman', 12))
        self.key1_skey.configure(font=('Times New Roman', 12))

        self.key1_frm.pack(ipady=self.grid_spacing)
        self.key1_current_prev.grid(row=0, column=0)
        self.key1_lkey.grid(row=2, column=0)
        self.key1_skey.grid(row=1, column=0)

        self.btn_frm = tk.Frame(master_frm)

        self.rec = tk.Label(self.btn_frm, text='Not recommended')
        self.rec.grid(row=0, column=1, padx=self.grid_spacing)

        self.B1 = tk.Button(self.btn_frm, text="Cancel",
                            command=self.cancelSave, width=20, height=1)
        self.B1.grid(row=1, column=0, padx=self.grid_spacing)

        self.B2 = tk.Button(self.btn_frm, text="Continue",
                            command=self.continueSave, width=20, height=1, bg='#0a0')
        self.B2.grid(row=1, column=1, padx=self.grid_spacing)
        self.btn_frm.pack(ipady=self.grid_spacing)

    def createEntryButtons(self):
        for i in scrolledfrm.winfo_children():
            i.destroy()
        for i in range(len(df)):
            date = str(df.loc[i, 'date'].strip('\n'))
            title = str(df.loc[i, 'title']).strip('\n')
            btn_txt = date+'\n'+title
            el = tk.Button(scrolledfrm, text=btn_txt,
                           command=lambda x=i: self.changeEntry(x))
            el.pack()

    def cancelSave(self):
        print('quit')
        self.popup.destroy()

    def continueSave(self):
        print('saved')
        saveTxt(skip=True)
        self.popup.destroy()


data = [
    [
        datetime.today().strftime('%m/%d/%y'),
        'Title',
        'Enter your text here.',
        'nan'
    ]
]
df = pd.DataFrame(data, columns=['date', 'title', 'text', 'last_updated'])


currentEntry = 0
prev_values = [-123, -432]
filename = 'newFile.csv'

window = tk.Tk()
window.title('Text Editor')
window.rowconfigure(1, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


# create elements
txt_frm = tk.Frame(window, bd=2, background='#24a')
frm_banner = tk.Frame(window, relief=tk.RAISED, bd=2,
                      height=20, background='#aaa')
frm_sidebar = tk.Frame(window, relief=tk.RAISED, bd=2, background='#222')

# text elements
txt_edit = tk.Text(txt_frm)
txt_edit.bind('<KeyRelease>', autosave_to_df)
txt_edit.configure(font=('Times New Roman', 12))
txt_edit.insert('1.0', 'Enter you text here')
font = tkfont.Font(font=txt_edit['font'])
tab_size = font.measure('    ')
txt_edit.config(tabs=tab_size)

skey = tk.Text(frm_banner, height=1, width=6)
skey.insert('1.0', '0')
lkey = tk.Text(frm_banner, height=1, width=6)
lkey.insert('1.0', '0')
title = tk.Text(frm_banner, height=1, width=15)
title.bind('<KeyRelease>', autosave_title_to_df)
title.insert('1.0', 'title')
title.configure(font=('Times New Roman', 10))




searchBar = tk.Text(frm_sidebar, width=15, height=1)
searchBar.insert('1.0', 'Search')
searchBar.bind('<KeyRelease>', search)

grdNames = tk.Frame(frm_sidebar, width=100)
grdTitle = tk.Label(grdNames, text='Title', width=10)
grdDate = tk.Label(grdNames, text='Created')
grdUpdate = tk.Label(grdNames, text='Updated')


# buttons
runKeys = tk.Button(frm_banner, text='Run', command=runKey)
save = tk.Button(frm_banner, text='Save', command=saveTxt)
refresh = tk.Button(frm_banner, text='Refresh', command=readCSV)
open = tk.Button(frm_banner, text='Open', command=openCSV)
deleteBtn = tk.Button(frm_banner, text='Delete', command=delete)
addBtn = tk.Button(frm_banner, text='Add', command=add)
saved_lbl = tk.Label(frm_banner, text='*Unsaved Document',
                     bg='#a00', fg='#fff', font=('Arial', 10))

# checkboxes
inverseEncoding = tk.IntVar()
inverseTypeEnc = tk.Checkbutton(frm_banner, text="type with inverse encoding",
                                variable=inverseEncoding,
                                onvalue=1,
                                offvalue=0,

                                width=20)
# SCROLLBARS
# sidebar
searchBar.grid(row=0, column=0, sticky='ew', pady=5)

grdNames.grid(row=1, column=0, sticky='nsew')
grdTitle.grid(row=0, column=0, sticky='nsew')
grdDate.grid(row=0, column=1, sticky='nsew', ipadx=10)
grdUpdate.grid(row=0, column=2, sticky='nsew')

sf = ScrolledFrame(frm_sidebar, width=200, height=500)
sf.grid(row=2, column=0, sticky='nsew')
# sf.pack(side="top", expand=1, fill="both")

# Bind the arrow keys and scroll wheel
sf.bind_arrow_keys(frm_sidebar)
sf.bind_scroll_wheel(frm_sidebar)
scrolledfrm = sf.display_widget(tk.Frame)
# scrolledfrm = tk.Frame(sf, height=200)
# scrolledfrm.grid(row=0, column=0, sticky='nsew')
# arrange elements

frm_sidebar.grid(row=0, column=0, rowspan=2, sticky='ns')
frm_banner.grid(row=0, column=1, sticky='ew')
txt_frm.grid(row=1, column=1, sticky='nsew')

# frm_sidebar.pack(fill=tk.Y)
# frm_banner.pack(fill=tk.X)
# txt_edit.pack(expand=True, fill=tk.BOTH)

txt_edit.pack(fill=tk.BOTH, expand=True, padx=2, pady=2, ipadx=5, ipady=5)
# banner bar
skey.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
lkey.grid(row=0, column=1, sticky="ew", padx=5)
title.grid(row=0, column=2, sticky="ew", padx=5)

save.grid(row=0, column=3, sticky='ew')
deleteBtn.grid(row=0, column=5)
addBtn.grid(row=0, column=6)
open.grid(row=0, column=4)
saved_lbl.grid(row=0, column=7, padx=10, ipadx=3, ipady=3)
setupFrame()
# txt_edit.insert('1.0', encode('hello world', chars, 43322, 233))
window.mainloop()

# write pandas dataframe
quit()

option = input('Read/Write: ')
if option == "r":
    with open('textEntry.txt', 'r') as tFile:
        key = input('=>').split(',')
        for i in tFile:
            text = encode(i.strip('\n'), chars, int(
                key[0]), int(key[1])).split('|')
            print('Date: ', text[0])
            print(text[1], '\n')

elif option == 'w':
    with open('textEntry.txt', 'a') as tFile:
        text = input('Enter text here: ')
        key = input('=>').split(',')
        print(key)
        tFile.writelines(encode(date+'|'+text, chars,
                         int(key[0]), int(key[1]))+'\n')

# 43322
# 233
