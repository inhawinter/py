# import urllib.request
#
# url = 'https://www.inha.ac.kr/sites/kr/images/logo.png'
# urllib.request.urlretrieve(url, 'inha.png')  # 웹에서 가져온 이미지를 보조기억장치 저장
# print('저장완료')

import urllib.request

url = 'https://www.inha.ac.kr/sites/kr/images/logo.png'
logo = urllib.request.urlopen(url).read()  # 이미지를 다운받아서 메모리에 저장

with open('inha.png', 'wb') as fp:
    fp.write(logo)
    print('저장완료')
