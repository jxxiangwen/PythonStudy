# coding: UTF-8
__author__ = 'jxxia'

import time, random
from multiprocessing.managers import BaseManager


SERVER_IP = '127.0.0.1'
SERVER_PROT = 9010


class ServerManager(BaseManager):
    pass

class Client(object):
    """客户端:处理任务"""

    def __init__(self):
        ServerManager.register("get_task_queue")
        ServerManager.register("get_result_queue")
        self._server_manager = ServerManager(
            address=(SERVER_IP, SERVER_PROT), authkey=b'z')

    def start(self):
        print "Client: Start."
        self._server_manager.connect()
        task_queue = self.task_queue
        result_queue = self.result_queue
        while not task_queue.empty():
            name = task_queue.get(timeout=1)
            print "Client: Get: %s" % name
            user = {"name": name, "age": random.randint(20, 26)}
            print "Client: Set: %s" % user
            result_queue.put(user)

    @property
    def task_queue(self):
        return self._server_manager.get_task_queue()

    @property
    def result_queue(self):
        return self._server_manager.get_result_queue()


if __name__ == "__main__":

    Client().start()
    # if has_in_argv(["-t", "--client", "client"]):
    #     Client().start()
    # elif has_in_argv(["-m", "--matser", "master"]):
    #     Master().start()
    # else:
    #     Server().start()