#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = 11  # 模块属性


def f():
    print(x)  # 函数内的本地变量


def g():
    x = 22  # 函数内的本地变量
    print(x)


class C:
    x = 33  # 类属性

    def m(self):
        x = 44  # 方法中的本地变量
        self.x = 55  # 实例属性


if __name__ == "__main__":
    print(x)
    f()
    g()
    print(x)
    obj = C()
    print(obj.x)
    obj.m()
    print(obj.x)
    print(C.x)

    # print(C.m.x) 无法读取方法中的本地变量
