#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any


traceMe = False


def trace(*args):
    if traceMe:
        print("[" + " ".join(map(str, args)) + "]")


def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs) -> None:
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace("get", attr)
                if attr in privates:
                    raise TypeError("private attribute fetch" + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr: str, value: Any) -> None:
                trace("set", attr, value)
                if attr == "wrapped":
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError("private attribute change: " + attr)
                else:
                    setattr(self.wrapped, attr, value)

                return onInstance

        return onDecorator


if __name__ == "__main__":
    traceMe = True

    @Private("data", "size")
    class Double:
        def __init__(self, label, start) -> None:
            self.label = label
            self.start = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print(f"{self.label} => {self.data}")

    X = Double("X is", [1, 2, 3])
    Y = Double("Y is", [-10, -20, -30])
