import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": (file),
    }
    instance.enqueue(content)
    print(content)
    return content


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')
    path_file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
