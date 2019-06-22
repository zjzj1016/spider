import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
print(HTML)
if farm1 in HTML:
    url1.append(HTML)
elif farm2 in HTML:
    url2.append(HTML)
elif farm3 in HTML:
    url3.append(HTML)
else:
    url4.append(HTML)
url=(url1,url2,url3,url4)
for HTML in url:
    response = requests.get(HTML)
    content = response.content
    print(content)
    with open(HTML,'wb') as f:
        f.write(content)



