groups = {
    '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
    '마마무': ['문별', '솔라', '휘인', '화사']
}

# print(groups['빅뱅'].pop(-1))
# print(groups)
# print(groups.pop('마마무'))
# print(groups)
# print(groups.pop('마마무'))   # key error
# print(groups)

# for group, members in groups.items():
#     print(f'{group}의 멤버')
#     for member in members:
#         if member != '승리':
#             print(member)

for temps in groups.items():
    print(f'{temps[0]}의 멤버')
    for member in temps[1]:
        if member != '승리':
            print(member)




'''
빅뱅의 멤버
GD
태양
탑
대성
마마무의 멤버
문별
솔라
휘인
화사
'''