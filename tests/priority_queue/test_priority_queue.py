from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    lista_arquvios = [
        {
            "nome_do_arquivo": "arquivo1",
            "qtd_linhas": 1,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo2",
            "qtd_linhas": 6,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo3",
            "qtd_linhas": 3,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo4",
            "qtd_linhas": 8,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo5",
            "qtd_linhas": 2,
            "linhas_do_arquivo": 'hahaha'
        },
    ]
    project_priority = PriorityQueue()

    for indexar in lista_arquvios:
        project_priority.enqueue(indexar)

    assert len(project_priority) == 5
    assert project_priority.search(0)["qtd_linhas"] == 1
    project_priority.dequeue()
    assert project_priority.search(0)["qtd_linhas"] == 3
    project_priority.dequeue()
    assert project_priority.search(0)["qtd_linhas"] == 2
    project_priority.dequeue()
    assert project_priority.search(0)["qtd_linhas"] == 6
    project_priority.dequeue()
    assert project_priority.search(0)["qtd_linhas"] == 8

    with pytest.raises(IndexError):
        project_priority.search(len(project_priority))
        for indexar in lista_arquvios:
            project_priority.enqueue(indexar)
        project_priority.search(1)["qtd_linhas"] == 6
