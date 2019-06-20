import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'啦啦啦'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)

data = bytes(urllib.parse.urlencode({'pw':'zj2456','acc':'2456752'}),enconding='utf8')
url = 'http://qzone.qq.com/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)
