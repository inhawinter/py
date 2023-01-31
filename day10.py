import urllib.request
import urllib.parse

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

id = input('지역코드 : ')  # 108 전국, 109 서울인천경기, 105 강원
values = {'stnId': id}
parameters = urllib.parse.urlencode(values)
url = api + '?' + parameters

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)