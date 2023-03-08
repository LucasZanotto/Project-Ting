from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.queue import Queue


class PriorityQueue(AbstractQueue):
    def __init__(self):
        self.regular_priority = Queue()
        self.high_priority = Queue()
        self.priority_limit = 5

    def is_priority(self, value):
        return value["qtd_linhas"] < self.priority_limit

    def __len__(self):
        return len(self.high_priority) + len(self.regular_priority)

    def enqueue(self, value):
        if self.is_priority(value):
            self.high_priority.enqueue(value)
        else:
            self.regular_priority.enqueue(value)

    def dequeue(self):
        if len(self.high_priority):
            return self.high_priority.dequeue()

        return self.regular_priority.dequeue()

    def search(self, index):
        if index < len(self.high_priority):
            return self.high_priority.search(index)
        return self.regular_priority.search(index - len(self.high_priority))


# project = Queue()
# # PriorityQueue.enqueue(project, {
# #      "nome_do_arquivo": "arquivo1",
# #      "qtd_linhas": 6,
# #      "linhas_do_arquivo": 'hahaha'
# #     })
# lista_arquvios = [
#     {
#      "nome_do_arquivo": "arquivo1",
#      "qtd_linhas": 1,
#      "linhas_do_arquivo": 'hahaha'
#     },
#     {
#      "nome_do_arquivo": "arquivo2",
#      "qtd_linhas": 6,
#      "linhas_do_arquivo": 'hahaha'
#     },
#     {
#      "nome_do_arquivo": "arquivo3",
#      "qtd_linhas": 3,
#      "linhas_do_arquivo": 'hahaha'
#     },
#     {
#      "nome_do_arquivo": "arquivo4",
#      "qtd_linhas": 8,
#      "linhas_do_arquivo": 'hahaha'
#     },
#     {
#      "nome_do_arquivo": "arquivo5",
#      "qtd_linhas": 2,
#      "linhas_do_arquivo": 'hahaha'
#     },
# ]
# project_priority = PriorityQueue()

# for indexar in lista_arquvios:
#     project_priority.enqueue(indexar)


# print(project_priority.search(0)["qtd_linhas"] == 1)
# project_priority.dequeue()
# print(project_priority.search(0)["qtd_linhas"] == 3)
# project_priority.dequeue()
# print(project_priority.search(0)["qtd_linhas"] == 2)
# project_priority.dequeue()
# print(project_priority.search(0)["qtd_linhas"] == 6)
# project_priority.dequeue()
# print(project_priority.search(0)["qtd_linhas"] == 8)
