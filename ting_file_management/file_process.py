import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text_list: list = txt_importer(path_file)
    infoDict: dict = {
        "name_path_file": path_file,
        "quantity_words": len(text_list)
    }
    instance.enqueue(infoDict)


def remove(instance):
    print('TTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    print(instance)
    print('TTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    if len(instance == 0):
        return sys.stderr.write('Posição inválida\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
