#!/bin/usr/env python
# -*- coding: utf-8 -*-
"""
生成校验码
https://honmaple.com/blog/view/29
"""

import os
import random

from PIL import Image, ImageFont, ImageDraw

_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

currentPath = os.path.split(os.path.realpath(__file__))[0]
fontType = os.path.join(currentPath, 'OpenSans-Bold.ttf')


def create_validate_code(size=(80, 30),
                         chars=init_chars,
                         img_type="PNG",
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(0, 0, 255),
                         font_size=18,
                         font_type=fontType,
                         length=4,
                         draw_lines=True,
                         n_line=(1, 2),
                         draw_points=True,
                         point_chance=2):
    width, height = size  # 图像的宽，高
    img = Image.new(mode, size, bg_color)  # 创建新图像
    draw = ImageDraw.Draw(img)
    c_chars = random.sample(chars, length)
    strs = ' %s ' % ' '.join(c_chars)  # 每个字符前后以空格隔开

    font = ImageFont.truetype(font_type, font_size)
    font_width, font_height = font.getsize(strs)

    draw.text(((width - font_width) / 3, (height - font_height) / 3), strs, font=font, fill=fg_color)

    img.save(os.path.join(currentPath, 'validate.png'), 'PNG')  # 存储图片


if __name__ == '__main__':
    create_validate_code()
