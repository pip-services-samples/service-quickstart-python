# -*- coding: utf-8 -*-

class HelloWorldController:
    __defaultName = None

    def __init__(self):
        self.__defaultName = "Pip User"

    def configure(self, config):
        self.__defaultName = config.get_as_string_with_default("default_name", self.__defaultName)

    def greeting(self, name):
        return f"Hello, {name if name else self.__defaultName} !"
