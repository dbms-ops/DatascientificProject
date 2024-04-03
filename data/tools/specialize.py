#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Super:
    def method(self):
        print("in Super.method")

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Extender(Super):
    def method(self):
        print("stating Extender.method")
        Super.method(self)
        print("ending Extender.method")


class Replacer(Super):
    def method(self):
        print("In Replace.method")


class Provider(Super):
    def action(self):
        print("in Provider.action")


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()
        print("\n Provider...")
        x = Provider()
        x.delegate()
