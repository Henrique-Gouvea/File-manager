import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file) as file:
            return file.read().splitlines()

    except FileNotFoundError:
        sys.stderr.write('Arquivo ' + path_file + ' não encontrado\n')


if __name__ == "__main__":
    txt_importer('statics/arquivo_teste.csv')
