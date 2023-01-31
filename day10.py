import urllib.request
from bs4 import BeautifulSoup

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
urls = urllib.request.urlopen(api).read()
soup = BeautifulSoup(urls, "html.parser")

cities = soup.find_all("city")
datas = soup.find_all("data")

for i in range(len(cities)):
    print(f'{cities[i].string}의 날씨는 {datas[i*13].find("wf").string}입니다.')


# import urllib.request
# from bs4 import BeautifulSoup
#
# api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
# urls = urllib.request.urlopen(api).read()
# soup = BeautifulSoup(urls, "html.parser")
#
# cities = soup.find_all("city")
# wfs = soup.find_all("wf")
# wfs.pop(0)  # 맨 앞의 wf태그 내용은 중기 날씨 요약 뉴스
#
# for i in range(len(cities)):
#     print(f'{cities[i].string}의 날씨는 {wfs[i*13].string}입니다.')
