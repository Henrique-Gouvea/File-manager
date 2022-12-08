from ting_file_management.file_process import process
from ting_file_management.queue import Queue
import re 


def exists_word(word, instance):
    list_word_found: list = []
    for file in instance.queue:
        ocorrency:list = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if len(re.findall(word, line, flags=re.IGNORECASE)) > 0:
                ocorrency.append({"linha": index + 1})
        if len(ocorrency) == 0:
            return []
        ocorrency_file: dict = {
            "palavra": word,
            "arquivo": file['nome_do_arquivo'],
            "ocorrencias": ocorrency,
        }
        list_word_found.append(ocorrency_file)
    return list_word_found


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     project = Queue()
#     process("statics/nome_pedro.txt", project)
#     word = exists_word("pedro", project)
