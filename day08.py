# class & object

class Pokemon:
    def __init__(self, name, owner, skills):  # constructor
        self.name = name  # attribute, field, member variable
        self.owner = owner
        self.skills = skills.split('/')  # list
        print(f'포켓몬 {name} 생성됨')

    def info(self):  # method (member function)
        """
        포켓몬 정보(주인, 이름, 기술들) 출력
        :return: void
        """
        print(f'{self.owner}의 포켓몬은 {self.name}입니다')
        for skill in self.skills:
            print(f'===========\n{skill}')
        print('===========')


p1 = Pokemon('피카츄', '한지우', '번개/100만볼트/전광석화')
p2 = Pokemon('꼬부기', '오바람', '거품/물대포/몸통박치기')
p3 = Pokemon('파이리', '나이기', '불기둥/화염발사')

p3.info()
p2.info()

