#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Employee:
    def __init__(self, name, salary=0) -> None:
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        """
        Gives a raise to the employee based on the provided percentage.

        Args:
            percent (float): The percentage by which to increase the salary.

        Returns:
            None
        """
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "do stuff")

    def __repr__(self) -> str:

        return f"<Employee: name={self.name}, salary = {self.salary}>"


class Chef(Employee):
    def __init__(self, name) -> None:
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "make foods")


class Server(Employee):
    def __init__(self, name) -> None:
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):

    def __init__(self, name) -> None:
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "make pizza")


if __name__ == "__main__":
    bob = PizzaRobot("bob")
    print(bob)
    bob.work()
    bob.give_raise(0.20)
    print(bob)

    for kcalss in [Employee, Chef, Server, PizzaRobot]:
        obj = kcalss(kcalss.__name__)
        obj.work()
