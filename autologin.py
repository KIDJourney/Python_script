import urllib 
import urllib2
import cookielib
import time

loginurl = ""
submiturl = ""

userdata = {}
userdata['user_id'] = ""
userdata['password'] = ""
userdata = urllib.urlencode(userdata)

postdata = {}
postdata['id'] = ""
postdata['language'] = ""
postdata['source'] = """"""
postdata['input_text'] = ''
postdata['out'] = ''
postdata = urllib.urlencode(postdata)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
loginreq = urllib2.Request(loginurl,userdata,headers)
logincontent = opener.open(loginreq)

