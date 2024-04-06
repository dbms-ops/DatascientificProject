#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListInstance:

    def __init__(self) -> None:
        return "<Instance of %s, address %s:\n%s>" % (
            self.__class__.__name__,
            id(self),
            self.__attrnames(),
        )

    def __attrnames(self):

        return "".join(
            "\tname %s=%s\n" % (attr, self.__dict__[attr])
            for attr in sorted(self.__dict__)
        )
