import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        # saida de erros sys.stderr
        return sys.stderr.write(f"""Arquivo {path_file} não encontrado\n""")
    if not path_file[-4:] == '.txt':
        return sys.stderr.write("Formato inválido")
    with open(path_file) as file:
        file_list = file.read().split("\n")
        # print(file_list)
        return file_list


# txt_importer('statics/arquivo_teste.txt')
