import random
import os
from PIL import ImageFont, Image, ImageDraw, ImageFilter


def auth_code():
    size = (185, 60)  # 图片大小
    font_list = list("0123456789abcdefghijklmnopqrstuvwxyz")  # 验证码范围
    c_chars = "  ".join(random.sample(font_list, 4))  # 4个+中间加个俩空格
    print(c_chars)
    img = Image.new("RGB", size, (33, 33, 34))  # RGB颜色
    draw = ImageDraw.Draw(img)  # draw一个
    #font = ImageFont.truetype("arial.ttf", 23)  # 字体
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
    img.save(f'./test_img/{c_chars}.png')


if __name__ == '__main__':
    if not os.path.exists('./test_img'):
        os.mkdir('./test_img')
    while True:
        auth_code()
        if len(os.listdir('./test_img')) >= 3000:
            break
