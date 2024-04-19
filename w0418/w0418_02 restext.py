import requests
url = "http://www.google.com/"
res = requests.get(url)
res.raise_for_status()

print("페이지의 글자수 : ",len(res.text))
print("페이지의 소스코드 : ",res.text)  #string


with open('google.html','w',encoding='utf8') as f:
    f.write(res.text)