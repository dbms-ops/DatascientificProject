#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from classtools import AttrDisplay


class Person(AttrDisplay):
    name = "lixun"

    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        return self.pay * int(self.pay * (1 + percent))


class Manager(Person):

    def __init__(self, name, pay=0) -> None:
        super().__init__(name, "mgr", pay)

    def give_raise(self, percent, bonus=0.10):
        super().give_raise(bonus + percent)


class Department:
    def __init__(self, *args) -> None:
        self.members = list(*args)

    def add_member(self, person: Person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


# 实现一个作为控制层的 manager
class Manager1:
    """通过 manager 实现一个控制类,"""

    def __init__(self, name, pay) -> None:

        self.person = Person(name, "mgr", pay)

    def give_raise(self, percent, bonus):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):

        return getattr(self.person, attr)

    def __str__(self):

        return str(self.person)


class ShardData:
    # 将非函数的对象赋值给类属性,就会产生数据属性,由所有实例共享
    name = "supei"


if __name__ == "__main__":
    # self-test code
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    # 不建议在类之外的硬编码进行类中元素的操作,会导致后续的开发者迷糊
    print(bob.last_name())
    print(sue.give_raise(1.10))

    tom = Manager("Tom Jones", 5000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)

    # 多态的应用
    # 为不同的对象,选择不同的方法调用,就是多态
    print("--ALL three")
    for obj in (bob, sue, tom):
        obj.give_raise(0.10)
        print(obj)

    # 定制构造函数
    mgr = Manager("Tom Jones", 5000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)

    tom_1 = ShardData()
    tom_2 = ShardData()

    print(tom_1.name)
    print(tom_2.name)
