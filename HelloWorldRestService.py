# -*- coding: utf-8 -*-
import bottle
from pip_services3_commons.refer import Descriptor
from pip_services3_commons.validate import Schema
from pip_services3_rpc.services import RestService


class HelloWorldRestService(RestService):

    def __init__(self):
        super(HelloWorldRestService, self).__init__()

        self._base_route = "/hello_world"

        ControllerDescriptor = Descriptor('hello-world', 'controller', '*', '*', '1.0')
        self._dependency_resolver.put('controller', ControllerDescriptor)
        self._controller = None

    def set_references(self, references):
        super(HelloWorldRestService, self).set_references(references)
        self._controller = self._dependency_resolver.get_one_required('controller')

    def register(self):
        self.register_route(method="GET", route="/greeting", schema=Schema(), handler=self.greeting)

    def greeting(self):
        name = bottle.request.query.get('name')
        result = self._controller.greeting(name)
        return self.send_result(result)
