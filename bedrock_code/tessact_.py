from PIL import Image
import pytesseract
import cv2
import os
from pytesseract import Output
import numpy as np
import matplotlib.pyplot as plt

def split_word(df, result, block):
    x_s = df['left'].values
    y_s = df['top'].values
    arr = [0]
    for i in range(len(x_s)-1):
        if abs(x_s[i] - x_s[i+1]) > 70 and abs(y_s[i] - y_s[i+1]<5):
            arr.append(i+1)
    arr.append(len(x_s))
    word_list = df['text'].values
    for i in range(len(arr)-1):
        df_temp = df[arr[i]:arr[i+1]]
        word_list = df_temp['text']
        
        text = ' '.join(word_list)
        x_min = min(df_temp['left'])
        y_min = min(df_temp['top'])
        x_max = max(df_temp['left']) + max(df_temp['width'])
        y_max = max(df_temp['top']) + max(df_temp['height'])
        if len(text)<50:
            d = {'coor': ((x_min, y_min), (x_max, y_max)), 'text': text}
            result.append(d)
    return None

path = '0.jpg'
def get_field(path):
    image = cv2.imread(path)
    # plt.imshow(image)
    # plt.show()
    # choices = ['full name', 'gender', 'date of birth', ]
    res = {'full_name': 'Thuan dep trai'}
    # print(image.shape)

    image = cv2.resize(image, (773, int(773*16/9)))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    df = pytesseract.image_to_data(gray, output_type=Output.DATAFRAME)
    df.dropna(subset=['text'], inplace=True)

    result = []

    for block in set(df['block_num']):
        df_temp = df[df['block_num']==block]
        word_list = df_temp['text']
        arr = split_word(df_temp, result, block)

    field = []
    for i in result:
        # print(i)
        coor = i['coor']
        if "Full name" in i['text']:
            field.append(('full_name', coor))
            print("Enter your full name?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Gender" in i['text']:
            field.append(('gender', coor))
            print("Enter your gender?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Date of birth" in i['text']:
            field.append(('birth', coor))
            print("Enter your birth?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Country of birth" in i['text']:
            field.append(('country_birth', coor))
            print("Enter your country of birth?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Country of citizenship" in i['text']:
            field.append(('citizen', coor))
            print("Enter your citizen?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Permanent home address" in i['text']:
            field.append(('per_add', coor))
            print("Enter your permanet home address?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Permanent home tel" in i['text']:
            field.append(('per_tel', coor))
            print("Enter your permanent home tel?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Email address" in i['text']:
            field.append(('email', coor))
            print("Enter your gender?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Father's name" in i['text']:
            field.append(('father_name', coor))
            print("Enter your father's name?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Mother's name" in i['text']:
            field.append(('mother_name', coor))
            print("Enter your mother's name?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Father's occupation" in i['text']:
            field.append(('father_occ', coor))
            print("Enter your mother's name?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        if "Mother's occupation" in i['text']:
            field.append(('mother_occ', coor))
            print("Enter your mother's name?")
            cv2.putText(image, input(), (coor[1][0]+10,coor[1][1]),  cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0))
        cv2.rectangle(image, coor[0], coor[1], (0, 255, 0), 1)
    os.remove(filename)
    cv2.imwrite('out.jpg', image)
    return field

# print(get_field(path))
get_field(path)