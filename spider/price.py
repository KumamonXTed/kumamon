import re
import urllib.request

from builtins import print

date = '2017-3-23'
url = 'http://flights.ctrip.com/booking/WNZ-HGH-day-1.html?DDate1='+date
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }

request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
html = response.read()
print(html)

content = response.read().decode('utf-8')
pattern = re.compile(r'<div.*?flight_logo">(.*?)</strong.*?span>(.*?)</span.*?'
                     + 'flight_logo">(.*?)</strong.*?span>(.*?)</span.*?'
                     + 'time">(.*?)</strong.*?<div>(.*?)</div.*?'
                     + 'stay-time">(.*?)</span.*?city-name">(.*?)</span.*?'
                     + 'time">(.*?)</strong>(.*?)<div>(.*?)</div.*?'
                     + '0">(.*?)</span.*?0">(.*?)</span.*?</dfn>(.*?)</span')

items = re.findall(pattern,content)
for item in items:
	next_day = re.search("+.*?", item[9])
	if not next_day:
		print("%s%s ,%s , %s%s , %s , %s(%s)->%s(%s) , %s(%s) , ￥%s"%(item[0], item[1], item[11], item[2] , item[3],item[12],item[5],item[4],item[10],item[8],item[7],item[6],item[13]))
	else:
		print("%s%s ,%s , %s%s , %s , %s(%s)->%s(%s)%s , %s(%s) , ￥%s"%(item[0], item[1], item[11], item[2], item[3], item[12], item[5], item[4], item[10], next_day, item[8], item[7], item[6], item[13]))