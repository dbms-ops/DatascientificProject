#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class AttrDisplay:

    def gatherAttrs(self):
        attrs = [f"{key}={getattr(self, key)}" for key in sorted(self.__dict__)]
        return ",".join(attrs)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}:{self.gatherAttrs()}]"


if __name__ == "__main__":

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self) -> None:
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    print(x)
    print(y)
