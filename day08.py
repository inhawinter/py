# class & object

class Pokemon:
    def __init__(self, owner, skills):  # constructor
        self.__owner = owner  # like private
        self.skills = skills.split('/')  # list
        import datetime  # 상속관계 x
        print(f'[{datetime.datetime.now()}] 포켓몬 생성됨 :', end=' ')

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def info(self):  # method (member function)
        """
        포켓몬 정보(주인, 이름, 기술들) 출력
        :return: void
        """
        print(f'{self.__owner}의 포켓몬은 {self.name}입니다')
        for skill in self.skills:
            print(f'===========\n{skill}')
        print('===========')


    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):  # class 자식클래스(부모클래스):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'[삐까삐까] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')


class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'[꼬북꼬북] {self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')

pika1 = Pikachu('한지우', '번개/100만 볼트')
ggo1 = Ggoboogi('오바람', '거품/물대포/몸통박치기')
# print(ggo1.owner)
# pika1.info()
pika1.attack(1)
ggo1.attack(2)


print(pika1.owner)  # __owner는 사용 불가, 프로퍼티를 통한 접근 가능
pika1.owner = '덴트'  # _Pokemon__owner = '덴트' , 사실상 다른 언어의 private을 지원하는게 아니기 때문에 _클래스이름__속성 형태로 접근 가능하다
print(pika1.owner)
print(pika1._Pokemon__owner)
