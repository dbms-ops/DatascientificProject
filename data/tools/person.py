#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Person:
    name = "lixun"

    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        return self.pay * int(self.pay * (1 + percent))

    def __str__(self) -> str:
        """
        重载 __str__ 运算符, 用于实例在进行打印时, 调用 __str__ 方法

        Returns:
            str: A string representation of the object.
        """

        return f"[Person: {self.name} {self.pay}]"


class Manager(Person):

    def give_raise(self, percent, bonus=0.10):
        super().give_raise(bonus + percent)


if __name__ == "__main__":
    # self-test code
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    # 不建议在类之外的硬编码进行类中元素的操作,会导致后续的开发者迷糊
    print(bob.last_name())
    print(sue.give_raise(1.10))

    tom = Manager("Tom Jones", "mgr", 5000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)

    # 多态的应用
    # 为不同的对象,选择不同的方法调用,就是多态
    print("--ALL three")
    for obj in (bob, sue, tom):
        obj.give_raise(0.10)
        print(obj)
