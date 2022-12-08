import sys
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance):

    for file in instance.queue:
        if file['nome_do_arquivo'] == path_file:
            return
    if (path_file):
        text_list: list = txt_importer(path_file)
        infoDict: dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_list),
            "linhas_do_arquivo": text_list
        }
        print(infoDict)
        instance.enqueue(infoDict)


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return

    data = instance.dequeue()
    file_name = data["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
    except IndexError:
        sys.stderr.write("Posição inválida")
