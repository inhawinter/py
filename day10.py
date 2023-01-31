from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="http://www.inha.ac.kr">인하대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""
# 인하대학교의 url주소는 http://www.inha.ac.kr입니다.
soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a")  # return list
# print(urls)
for url in urls:
    print('{0}의 url주소는 {1}입니다.'.format(url.string, url.attrs['href']))
    # univ = url.string
    # link = url.attrs['href']
    # print('{0}의 url주소는 {1}입니다.'.format(univ, link))



# from bs4 import BeautifulSoup
#
# html = """
# <html>
# <head>
# <title>스크레이핑 실습</title>
# </head>
# <body>
# <h1 id="univ">인하대학교</h1>
# <p>웹스크레이핑</p>
# <p id="contents">파이썬 기본 문법, 판다스, GUI ... </p>
# </body>
# </html>
# """
#
# soup = BeautifulSoup(html, 'html.parser')
# university = soup.find(id='univ')
# contents = soup.find(id='contents')
#
# print(contents.string)
# print(university.string)