def exists_word(word, instance):
    """Aqui irá sua implementação"""
    ocorre = []
    lines = []
    for index in range(len(instance)):
        file_info = instance.search(index)
        for instance, line in enumerate(file_info["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                lines.append({"linha": instance + 1})
        if len(lines) > 0:
            ocorre.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": lines,
                }
            )
    return ocorre


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
