class Hero:
    def __init__(self, name, power, attack, armor, skill, quantity):
        '''
        :param name: 名字
        :param power: 血量
        :param attack: 攻击
        :param armor: 护甲
        :param skill: 技能
        '''
        self.name = name
        self.power = power
        self.attack = attack
        self.armor = armor
        self.skill = skill
        self.quantity = 100
#实例对象
hero1=Hero("盖伦",1000,50,150,
           {"致命打击":{"伤害":100,"quantity":10},
            "审判":{"伤害":100,"quantity":10},
            "德玛西亚正义":{"伤害":100,"quantity":10}})
hero2=Hero("后裔",800,150,70,
           {

           })