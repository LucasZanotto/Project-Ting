import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    files = txt_importer(path_file)
    qtd_linhas = len(files)
    # print(files)
    dict_padrao = {
           "nome_do_arquivo": path_file,
           "qtd_linhas": qtd_linhas,
           "linhas_do_arquivo": files
           }
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    instance.enqueue(dict_padrao)
    sys.stdout.write(str(dict_padrao))


if __name__ == "__main__":
    project = Queue()
    process("statics/arquivo_teste.txt", project)


def remove(instance: Queue):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None
    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    sys.stdout.write(f"""Arquivo {path_file} removido com sucesso\n""")


def file_metadata(instance, position):
    if len(instance) < position:
        sys.stderr.write("Posição inválida\n")
        return None
    path_file = instance.search(position)
    instance.dequeue()
    sys.stdout.write(str(path_file))
