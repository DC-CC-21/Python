# import tkinter as tk
# from tkinter import ttk
# # from Python.peachProject import openCSV
# import peachProject as pP

# inventory = pP.openCSV()
# btns = []


# def add(self, idx):
#     print(self)

# def createStore():
#     for i in range(len(inventory)):
#         frm = tk.Frame(bg='black', width='200', height='200')
#         frm.grid(row=0, column=i, padx=10, pady=10)

#         label = ttk.Label(master=frm, text='Your\nImage')
#         label.pack()
        
#         per = ttk.Button(master=frm, text='Click to Personalize')
#         per.pack()

#         btn = ttk.Button(master=frm, text=f'{inventory[i][0]} ${inventory[i][-1]}\nAdd to Cart', command=lambda: add(inventory[i][0], i))
#         btn.pack(side=tk.BOTTOM)

#         btns.append([label, per, btn, inventory[0]])

# def main():
#     root = tk.Tk()
#     root.geometry('800x500')
#     createStore()
#     root.mainloop()

# main()


# from PIL import Image
# import numpy as np
# import pandas as pd

# img = Image.open('images/Blue Sky.jpg')
# img = np.array(img).flatten()
# np.savetxt('np.csv', img, delimiter=',')

from PIL import Image
from numpy import array, moveaxis, indices, dstack
import pandas as pd
from PIL import Image

# image = Image.open("images/Blue Sky.jpg")
# pixels = image.convert("RGB")
# rgbArray = array(pixels.getdata()).reshape(image.size + (3,))
# indicesArray = moveaxis(indices(image.size), 0, 2)
# allArray = dstack((indicesArray, rgbArray)).reshape((-1, 5))


# df = DataFrame(allArray, columns=["y", "x", "red","green","blue"])
# print(df.head())
# df.to_csv("data.csv",index=False)

def turn_img_to_csv(path):
    img = Image.open(f'images/{path}.jpg')
    pix = img.load()
    width, height = img.size

    df = pd.DataFrame(data=[], columns=[i for i in range(width)], index=[j for j in range(height)])

    df.iloc[0,0] = 100
    
    for i in range(df.shape[1]):
        for j in range(df.shape[0]):
            r,g,b = pix[i,j]
            df.loc[j,i] = f'{r},{g},{b}'


    df.to_csv(f'{path}.csv')
turn_img_to_csv('Blue Sky')

def turn_csv_to_img(path):
    df = pd.read_csv(f'{path}.csv', header=None, index_col=False)

    img = Image.new('RGB', (df.shape[1]-1, df.shape[0]-1), 0)
    pix = img.load()
    width, height = img.size

    for i in range(1, width+1):
        for j in range(1, height+1):
            lst = df.loc[j,i].split(',')
            pix[i-1,j-1] = (int(lst[0]), int(lst[1]), int(lst[2]))
    return img
img = turn_csv_to_img('Blue Sky')
img.show()


# a = pd.read_csv('data.csv')

# image = {}
# for i in range(len(a['x'])):
#     # image.append((a.loc[i,'red'], a.loc[i,'green'], a.loc[i,'blue']))

#     image[a.loc[i,'x']][a.loc[i,'y']] = [a.loc[i,'red'], a.loc[i, 'green'], a.loc[i,'blue']]

# print(a.head(5))
# print(a.loc[0,a.columns[1]])
# print(image[:5])

# import numpy as np

# print(np.array(Image.open('images/Blue Sky.jpg'))[:5])

# # image = np.array(image).reshape(282,179, 3)
# # img = Image.fromarray(image)
# # img.save('my.png')
# # img.show()



