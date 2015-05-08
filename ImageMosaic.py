#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\Python\PIL\test.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-01-03
from PIL import Image , ImageDraw
import os
file = Image.open('test.png')
finalFile = Image.new("RGB",file.size,"white")
pixel = file.load()
draw = ImageDraw.Draw(finalFile)
squer = 10
for sx in range(0,400,squer) :
    for sy in range(0,400,squer) :
        colorDic = {}
        for x in range(sx,sx+squer) :
            for y in range(sy,sy+squer) :
                if colorDic.has_key(pixel[x,y]) :
                    colorDic[pixel[x,y]] += 1
                else :
                    colorDic[pixel[x,y]] = 1
        colorDic = sorted(colorDic,key = lambda value :value[1],reverse = True)
        color  = list(colorDic)[0]
        draw.rectangle((sx,sy,sx+squer,sy+squer),color)

finalFile.save(os.getcwd()+'/finish.jpg','JPEG')