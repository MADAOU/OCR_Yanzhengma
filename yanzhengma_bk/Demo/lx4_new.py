# from lx2 import *
from lx3_new import *
import random
import os
import re
import cv2
from PIL import ImageFont, Image, ImageDraw, ImageFilter


def auth_code():
    size = (185, 60)  # 图片大小
    font_list = list("0123456789abcdefghijklmnopqrstuvwxyz")  # 验证码范围
    c_chars = "  ".join(random.sample(font_list, 4))  # 4个+中间加个俩空格
    print(c_chars)
    img = Image.new("RGB", size, (33, 33, 34))  # RGB颜色
    draw = ImageDraw.Draw(img)  # draw一个
    # font = ImageFont.truetype("arial.ttf", 23)  # 字体
    font = ImageFont.truetype("arial.ttf", 30)  # 字体
    draw.text((5, 4), " "+c_chars, font=font, fill="white")  # 字颜色
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              0.002]
    img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img.save(f'./test_data_img/{c_chars}.png')


"""if __name__ == '__main__':
    if not os.path.exists('./test_data_img'):
        os.mkdir('./test_data_img')
    while True:
        auth_code()
        if len(os.listdir('./test_data_img')) >= 300:
            break"""


def sliceImg(img_path):
    if not os.path.exists('test_split_img'):
        os.mkdir('test_split_img')
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    eroded = cv2.erode(thresh, kernel)
    img_path = img_path.replace(' ', '').split('.')[0]
    contours, hierarchy = cv2.findContours(
        eroded, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours, _ = sort_contours(contours)
    group = []
    for i in range(1, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        temp = img[y:(y + h), x:(x + w)]
        group.append(knn_shib(temp)[0])
    return group


def actual_rate(group, file_name):
    file_name = re.sub("\s+", '', file_name)
    flg = True if ''.join(group) == file_name else False
    if not flg:
        print("file_name: " + file_name, "predict_name: "+''.join(group))
    return flg


if __name__ == '__main__':
    test_data_img = r'test_data_img'
    result = []
    total = 0
    actual = 0
    for test_file in os.listdir(test_data_img):
        group = sliceImg(test_data_img+f"/{test_file}")
        result.append(group)
        total += 1
        if actual_rate(group, test_file[:-4]):
            actual += 1

    print(result)
    print(float(actual/total))
