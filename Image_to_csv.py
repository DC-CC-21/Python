from PIL import Image
from numpy import array, moveaxis, indices, dstack
import pandas as pd
from PIL import Image

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
