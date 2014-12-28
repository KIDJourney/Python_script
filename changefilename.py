#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: KIDJourney
# @Date:   2014-12-28
# @Last Modified by:   KIDJourney
# @Last Modified time: 2014-12-28
import os,sys
standardname = "2014-07-23_"
filenames = os.listdir(os.getcwd())
print filenames
# for i in range(len(filenames)) :
#     os.rename(os.getcwd()+os.sep+filenames[i],standardname+("%.5d" % i)+'.jpg')