# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue
import re 


def construct_object(index, line, type):
    if(type == "linha"):
        return {"linha": index + 1}
    return {
        "linha": index + 1,
        "conteudo": line
        }


def search_exist_word(word, instance, type):
    list_word_found: list = []
    for file in instance.queue:
        ocorrency: list = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if len(re.findall(word, line, flags=re.IGNORECASE)) > 0:
                ocorrency.append(construct_object(index, line, type))
        if len(ocorrency) == 0:
            return []
        ocorrency_file: dict = {
            "palavra": word,
            "arquivo": file['nome_do_arquivo'],
            "ocorrencias": ocorrency,
        }
        list_word_found.append(ocorrency_file)
    return list_word_found


def exists_word(word, instance):
    return search_exist_word(word, instance, "linha")


def search_by_word(word, instance):
    return search_exist_word(word, instance, '')


# if __name__ == "__main__":
#     project = Queue()
#     process("statics/nome_pedro.txt", project)
#     word = exists_word("pedro", project)
