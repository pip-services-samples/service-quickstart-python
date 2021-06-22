# -*- coding: utf-8 -*-

from pip_services3_container.ProcessContainer import ProcessContainer
from pip_services3_rpc.build import DefaultRpcFactory

from HelloWorldServiceFactory import HelloWorldServiceFactory


class HelloWorldProcess(ProcessContainer):

    def __init__(self):
        super(HelloWorldProcess, self).__init__('hello-world', 'HelloWorld microservice')
        self._config_path = './config.yaml'
        self._factories.add(HelloWorldServiceFactory())
        self._factories.add(DefaultRpcFactory())
