#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: C:\Users\KIDJourney\Desktop\autologin.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-04-03
import urllib2
import urllib
import cookielib
import bs4 as bs
import re

class login() :
    def __init__(self):
        pass
    def wifilogin(self):
        url = "http://172.19.255.150/"
        userdata = {}
        userdata["DDDDD"] = ""
        userdata["upass"] = ""
        userdata["R1"] = "0"
        userdata["R2"] = "1"
        userdata["prar"]  ="00"
        userdata["0MKKey"] = "123456"
        userdata = urllib.urlencode(userdata)

        cj = cookielib.CookieJar()
        opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
        loginrep = urllib2.Request(url,userdata,headers)
        logincontent = opener.open(loginrep)
        soup = bs.BeautifulSoup(logincontent.read())
        # print soup

    def writedlogin(self):
        url = "http://222.195.191.231:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&session=null"
        userdata = {}
        userdata["DDDDD"] = "1307010412@upc"
        userdata['upass'] = ""
        userdata['R1'] = "0"
        userdata['R2'] = ""
        userdata['R6'] = "0"
        userdata['para'] = "00"
        userdata['0MKKey'] = "123456"
        userdata = urllib.urlencode(userdata)

        cj = cookielib.CookieJar()
        opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
        loginrep = urllib2.Request(url,userdata,headers)
        logincontent = opener.open(loginrep)
        soup = bs.BeautifulSoup(logincontent.read())
        # print soup

    def main(self) :
        try :
            self.wifilogin()
            self.writedlogin()
        except e :
            pass

job = login()
job.main()