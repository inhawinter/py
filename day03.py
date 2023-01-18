# list

bigbang = ['지디', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']
# exo.append('시우민')
exo.insert(1, '시우민')
print(exo)
# exo.extend(bigbang)
# exo = exo + bigbang

exo.append(bigbang)
print(exo)
# 태양
print(exo[-1][1])
print(exo[3][1])
print(exo[3][-4])
print(exo[3].pop())  # 승리 return 후 pop
print(exo)
print(exo[3].pop(2))  # 탑 return 후 pop
print(exo)
# exo.remove('대성')  # exo 리스트에서 대성을 찾을 수 없음
exo[3].remove('대성')  # 대성 remove
print(exo)
del exo[2]  # 첸 delete
print(exo)
exo.clear()
print(exo)