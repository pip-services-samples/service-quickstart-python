# -*- coding: utf-8 -*-

from pip_services3_commons.refer import Descriptor
from pip_services3_components.build import Factory

from HelloWorldController import HelloWorldController
from HelloWorldRestService import HelloWorldRestService


class HelloWorldServiceFactory(Factory):
    def __init__(self):
        super(HelloWorldServiceFactory, self).__init__()

        ControllerDescriptor = Descriptor('hello-world', 'controller', 'default', '*', '1.0')
        HttpServiceDescriptor = Descriptor('hello-world', 'service', 'http', '*', '1.0')

        self.register_as_type(ControllerDescriptor, HelloWorldController)
        self.register_as_type(HttpServiceDescriptor, HelloWorldRestService)
