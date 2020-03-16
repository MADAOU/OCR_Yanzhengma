import os
import time
import cv2
import random
import numpy as np


def read_img():
    img_array = []
    # img_lable = []
    file_list = os.listdir('./test_img')
    for file in file_list:
        try:
            image = file
            # img_name = file.replace(' ','').split('.')[0]
            img_array.append(image)
            # img_lable.append(img_name)
        except:
            print(f'{file}:图像已损坏')
            os.remove('./test_img/'+file)
    return img_array


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0
    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


def sliceImg(img_path):
    img = cv2.imread('./test_img/'+img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    eroded = cv2.erode(thresh, kernel)
    img_path = img_path.replace(' ', '').split('.')[0]
    # cv2.imwrite("./result1/" + img_path + ".png", eroded)
    contours, hierarchy = cv2.findContours(
        eroded, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours, _ = sort_contours(contours)
    print(img_path)
    if len(contours) == 5:
        for i in range(1, len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            temp = img[y:(y + h), x:(x + w)]
            if not os.path.exists(f'./train_data_img/{img_path[i-1]}/'):
                os.mkdir(f'./train_data_img/{img_path[i-1]}/')
            cv2.imwrite(f'./train_data_img/{img_path[i-1]}/' + str(
                time.time()) + '-' + str(random.randint(1, 10)) + '.png', temp)

#    for c in contours:
#        x, y, w, h = cv2.boundingRect(c)
#        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
#        temp = img[y:(y + h), x:(x + w)]
#        cv2.imwrite("./result/" + str(time.time()) + ".png", temp)


if __name__ == '__main__':
    img_array = read_img()
    for i in img_array:
        # print(i)
        sliceImg(i)
