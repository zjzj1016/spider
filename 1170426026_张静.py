def power(x):
x='啦啦'
data = urllib.parse.urlencode({'wd':'啦啦'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)