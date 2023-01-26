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


class Pikachu(Pokemon):  # class 자식클래스(부모클래스):
    pass


pika1 = Pikachu('피카츄', '한지우', '번개/50만 볼트/100만 볼트/전광석화')
pika1.info()
p1 = Pokemon('꼬부기', '오바람', '거품/몸통박치기')
p1.info()