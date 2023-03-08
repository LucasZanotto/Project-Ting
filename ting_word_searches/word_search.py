from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    lista = []
    for index in range(len(instance)):
        linhas = []
        frases = instance.search(index)["linhas_do_arquivo"]
        arquivo = instance.search(index)["nome_do_arquivo"]
        for linha, frase in enumerate(frases):
            if word.lower() in frase.lower():
                linhas.append({"linha": linha + 1})
        result = {
                    "palavra": word,
                    "arquivo": arquivo,
                    "ocorrencias": linhas
                 }
        if bool(linhas) is False:
            continue
        lista.append(result)
    return lista


def search_by_word(word, instance):
    lista = []
    for index in range(len(instance)):
        linhas = []
        frases = instance.search(index)["linhas_do_arquivo"]
        arquivo = instance.search(index)["nome_do_arquivo"]
        for linha, frase in enumerate(frases):
            if word.lower() in frase.lower():
                linhas.append({"linha": linha + 1, "conteudo": frase})
        result = {
                    "palavra": word,
                    "arquivo": arquivo,
                    "ocorrencias": linhas
                 }
        if bool(linhas) is False:
            continue
        lista.append(result)
    return lista
